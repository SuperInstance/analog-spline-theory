# analog-spline-theory

Formal proofs in analog spline theory: **Shipwright's Theorem** and the **Galois Connection** between physical and computational battens.

## Overview

This repository contains the formalization and proof chain for analog spline theory — the mathematical framework connecting physical wooden battens (used in shipbuilding) to computational spline curves. The central result establishes a Galois connection between the physical batten's Euler–Bernoulli beam deflection and the computational batten's piecewise quadratic Bézier representation.

## Key Results

- **Shipwright's Theorem** — Proves that a physical batten resting on pins produces deflections equivalent (within boundable error) to a computational batten's piecewise quadratic Bézier curve. Proven by DeepSeek v4-pro, surviving adversarial review by multiple frontier models.
- **Galois Connection** — Establishes a categorical adjunction between the physical and computational domains, showing that approximation in one direction preserves constraint satisfaction in the other.

## Contents

| File | Description |
|------|-------------|
| [`shipwright-theorem-formal.md`](shipwright-theorem-formal.md) | Formal statement and proof of Shipwright's Theorem |
| [`deepseek-formal-proofs.md`](deepseek-formal-proofs.md) | Full formal proof chain with detailed derivations |
| [`SYNTHESIS.md`](SYNTHESIS.md) | Synthesized summary of the theory |
| [`opus-ideation.md`](opus-ideation.md) | Early ideation and motivation |
| [`ADVERSARIAL-SYNTHESIS.md`](ADVERSARIAL-SYNTHESIS.md) | Adversarial review results |
| [`FINAL-5-MODEL-SYNTHESIS.md`](FINAL-5-MODEL-SYNTHESIS.md) | Cross-model consensus synthesis |
| [`flash-debate.md`](flash-debate.md) | Flash model debate transcript |
| [`seed-debate.md`](seed-debate.md) | Seed model debate transcript |
| [`nemotron-debate.md`](nemotron-debate.md) | Nemotron model debate transcript |
| [`galois-connection-proof.md`](galois-connection-proof.md) | Standalone Galois connection proof |
| [`galois-connection-proof-deepseek.md`](galois-connection-proof-deepseek.md) | DeepSeek's Galois connection proof |
| [`flux_galois_coq.v`](flux_galois_coq.v) | Coq formalization of the Galois connection |
| [`galois-unification-visualizer.py`](galois-unification-visualizer.py) | Python visualizer for Galois unification |
| [`SPLINE-PHYSICS-SYNERGY.md`](SPLINE-PHYSICS-SYNERGY.md) | Spline physics connections |
| [`HPDF-PPDF-SPLINE-RETRIEVAL.md`](HPDF-PPDF-SPLINE-RETRIEVAL.md) | HPDF/PPDF spline retrieval analysis |

## Connection to Conservation Spectral Analysis

Analog spline theory connects to the broader conservation spectral ecosystem through the **Galois connection** between physical constraint surfaces and their computational representations. Just as the Shipwright's Theorem establishes bounded correspondence between physical battens and Bézier curves, conservation spectral analysis maps physical conservation laws to discrete spectral signatures. The shared mathematical structure — constraint lattices, categorical adjunctions, and certifiable approximation — provides a unified framework for understanding how continuous physical phenomena embed into discrete computational systems.

## Provenance

Extracted from the [forgemaster](https://github.com/SuperInstance/forgemaster) `retro-sunset-plato` branch. Developed as part of the Retro Sunset Plato research program.
