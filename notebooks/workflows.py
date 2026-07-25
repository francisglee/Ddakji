# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo", "networkx", "matplotlib"]
# ///
"""Render process/workflows/*.toml state machines as diagrams.

Generated views of the workflow data (Layering Rule) — output goes to
assets/generated/<name>.png. Run headless: uv run --script notebooks/workflows.py
"""

import marimo

app = marimo.App()


@app.cell
def _():
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(ROOT / "tools"))
    import lib

    import matplotlib.pyplot as plt
    import networkx as nx

    OUT = ROOT / "assets" / "generated"
    OUT.mkdir(parents=True, exist_ok=True)
    return OUT, lib, nx, plt


@app.cell
def _(OUT, lib, nx, plt):
    def render(name: str):
        wf = lib.load_workflow(name)
        g = nx.DiGraph()
        for s in wf.get("states", wf.get("stages", [])):
            g.add_node(s)
        for t in wf.get("transition", []):
            g.add_edge(t["from"], t["to"], label=t.get("gate", t.get("via", "")))
        if not g.edges and "stages" in wf:
            stages = wf["stages"]
            for a, b in zip(stages, stages[1:]):
                g.add_edge(a, b)

        fig, ax = plt.subplots(figsize=(9, 4.5))
        pos = nx.spring_layout(g, seed=7) if len(g) > 5 else {
            s: (i, 0) for i, s in enumerate(g.nodes)
        }
        nx.draw_networkx_nodes(g, pos, ax=ax, node_size=2600, node_color="#e8eef7")
        nx.draw_networkx_labels(g, pos, ax=ax, font_size=9)
        nx.draw_networkx_edges(g, pos, ax=ax, connectionstyle="arc3,rad=0.15",
                               arrows=True, arrowsize=16)
        nx.draw_networkx_edge_labels(
            g, pos, ax=ax, font_size=7, label_pos=0.5,
            edge_labels={(u, v): d["label"] for u, v, d in g.edges(data=True) if d.get("label")},
        )
        ax.set_title(wf["name"])
        ax.axis("off")
        out = OUT / f"{wf['name']}.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return out

    outputs = [render(n) for n in ("scene-status", "idea-lifecycle", "publish-pipeline")]
    outputs
    return


if __name__ == "__main__":
    app.run()
