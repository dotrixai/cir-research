"""Regenerate the public figures from results/*.csv and the values listed below.

Usage: python figures/make_figures.py   (needs matplotlib)
"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
INK, MUTED, GRID = "#141413", "#5e5d59", "#d1cfc5"
A, B = "#c0582b", "#2a6fb0"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "svg.fonttype": "none", "svg.hashsalt": "cir",
})


def cost_to_q():
    rows = [r for r in csv.DictReader(open(RESULTS / "cost-to-q.csv", encoding="utf8")) if r["session"] == "R78"]
    series = [
        ("A010", "D1", A, "-", "o", "A010 vs gated local-global TF (D1)"),
        ("A019", "D1", B, "-", "o", "A019 vs gated local-global TF (D1)"),
        ("A010", "D2", A, "--", "s", "A010 vs TF-LG + same n-gram heads (D2)"),
        ("A019", "D2", B, "--", "s", "A019 vs TF-LG + same n-gram heads (D2)"),
    ]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for gate, label in [(1.0, "parity"), (0.75, "signal gate"), (0.5, "interesting gate")]:
        ax.axhline(gate, color=MUTED, lw=0.8, ls=":")
        ax.text(390, gate + 0.012, label, color=MUTED, fontsize=8)
    for cand, den, color, ls, marker, label in series:
        pts = sorted((int(r["q_baseline_updates"]), float(r["cost_ratio"])) for r in rows
                     if r["candidate"] == cand and r["denominator"] == den)
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=color, ls=ls, marker=marker, ms=5, lw=1.8, label=label)
        ax.annotate(f"{ys[-1]:.2f}", (xs[-1], ys[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=8, color=INK)
    ax.set_xticks([375, 500, 750, 1000, 1250, 1500])
    ax.set_xlim(340, 1580)
    ax.set_ylim(0.3, 1.2)
    ax.set_xlabel("Q = baseline's BPB after N updates")
    ax.set_ylabel("cost ratio (below 1 favors CIR)")
    ax.grid(axis="y", color=GRID, lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0, -0.16), ncol=2)
    ax.set_title("Cost to matched quality, one cost session (R78), seed 11. ESTIMATED.", fontsize=10, loc="left", color=INK)
    fig.tight_layout()
    fig.savefig(HERE / "cost-to-q.svg", metadata={"Date": None})
    plt.close(fig)


def baseline_history():
    # A010 cost to the baseline's final BPB, as the baseline was strengthened; last row is
    # the cheapest hybrid against the frontier baseline.
    # (label, low, high, seeds, evidence). Values from different cost sessions; ESTIMATED.
    data = [
        ("TFSR, Muon (27 Sep)", 0.570, 0.570, 1, "I188"),
        ("gated full attention (30 Sep)", 0.587, 0.625, 2, "I203"),
        ("gated local-global (1 Oct)", 0.633, 0.643, 2, "I211"),
        ("local-global + n-gram heads, D2 (3 Oct)", 1.06, 1.06, 1, "I240"),
        ("B1A, one attention layer (3-4 Oct)", 1.23, 1.27, 1, "I242, I248"),
        ("A025 (thin hybrid) vs B1A (4 Oct)", 0.949, 0.985, 1, "I251, I252"),
    ]
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    for i, (label, lo, hi, seeds, ev) in enumerate(data):
        y = len(data) - 1 - i
        ax.plot([0, lo], [y, y], color=GRID, lw=1, zorder=1)
        ax.plot([lo, hi], [y, y], color=A, lw=6, solid_capstyle="round", zorder=2)
        ax.plot([lo, hi], [y, y], "o", color=A, ms=7, zorder=3)
        text = f"{lo:.3g}" if lo == hi else f"{lo:.3g} to {hi:.3g}"
        ax.text(hi + 0.05, y, f"{text}  ({seeds} seed{'s' if seeds > 1 else ''}, {ev})", va="center", fontsize=8, color=INK)
    ax.axvline(1.0, color=MUTED, lw=0.8, ls=":")
    ax.axvline(0.75, color=MUTED, lw=0.8, ls=":")
    ax.text(1.0, len(data) - 0.45, "parity", color=MUTED, fontsize=8, ha="center")
    ax.text(0.75, len(data) - 0.45, "signal", color=MUTED, fontsize=8, ha="center")
    ax.set_yticks(range(len(data)))
    ax.set_yticklabels([d[0] for d in reversed(data)], fontsize=8)
    ax.set_xlim(0, 2.1)
    ax.set_ylim(-0.6, len(data) - 0.2)
    ax.set_xlabel("CIR cost to baseline's final BPB (below 1 favors CIR), ESTIMATED")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title("CIR cost ratio as the Transformer baseline was strengthened", fontsize=10, loc="left", color=INK)
    fig.tight_layout()
    fig.savefig(HERE / "baseline-history.svg", metadata={"Date": None})
    plt.close(fig)


def counted_path():
    # Counted organization: training cost to TF-LGN's final quality, average of EN and ID,
    # corrected (I313). Bars start at zero; ranges are the two seeds where available.
    rows = list(csv.DictReader(open(RESULTS / "counted-path.csv", encoding="utf8")))
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    for i, r in enumerate(rows):
        y = len(rows) - 1 - i
        lo, hi = float(r["low"]), float(r["high"])
        ax.barh(y, hi, color=GRID, height=0.5, zorder=1)
        ax.barh(y, lo, color=A, height=0.5, zorder=2)
        text = f"{lo:g}" if lo == hi else f"{lo:g} to {hi:g}"
        seeds = int(r["seeds"])
        ax.text(hi + 0.004, y, f"{text}  ({seeds} seed{'s' if seeds > 1 else ''}, {r['evidence']})", va="center", fontsize=8, color=INK)
    for gate, label in [(0.10, "0.10 gate"), (0.20, "0.20 gate")]:
        ax.axvline(gate, color=MUTED, lw=0.8, ls=":")
        ax.text(gate, len(rows) - 0.4, label, color=MUTED, fontsize=8, ha="center")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r["label"] for r in reversed(rows)], fontsize=8)
    ax.set_xlim(0, 0.32)
    ax.set_ylim(-0.6, len(rows) - 0.1)
    ax.set_xlabel("training cost to TF-LGN quality, x TF-LGN, average EN+ID (ESTIMATED)")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title("Counted organization (generic, D1), step by step", fontsize=10, loc="left", color=INK)
    fig.tight_layout()
    fig.savefig(HERE / "counted-path.svg", metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    cost_to_q()
    baseline_history()
    counted_path()
    print("wrote", HERE / "cost-to-q.svg", HERE / "baseline-history.svg", HERE / "counted-path.svg")
