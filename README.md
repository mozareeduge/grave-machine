# Grave-Machine

A bilingual generative e-poem by Mozare.

**Live work:** https://theblackbirdfield.com/works/grave-machine/run/  
**Portfolio entry:** https://theblackbirdfield.com/works/grave-machine/  
**Release:** v1.1.0 — English / Persian

---

*Grave-Machine* enters the *Taroko Gorge* remix tradition through burial, paperwork, and unfinished return. It is grounded in Mohammad Zare’s play *Grave*, whose dramatic world places bodily remains and administrative processing inside the same environment.

The browser holds two related surfaces. The generated poem continues on one side. A quieter runtime trace remains beside it, recording how each line arrived. The English and Persian versions share one release file while retaining different grammatical devices, material banks, language direction, and typographic proportions.

Generation comes from authored materials, routes, constraints, and probabilities. No language model writes the runtime text.

## Public artifact

`index.html` is the exact public bilingual v1.1 runtime preserved from the portfolio release.

SHA-256:

```text
0e1cfd0097cf261f169c0e52a88d39f1541f04f07d179b1f009ff2cc311eb385
```

The canonical live work remains inside The Black Bird Field portfolio. This repository is the public source archive and release record; GitHub Pages is intentionally not enabled here.

## Opening locally

Open `index.html` in a modern browser, or serve the directory:

```bash
python3 -m http.server 8000
```

The file runs without a build step. Persian typography requests Estedad from jsDelivr and retains system fallbacks if the font cannot be fetched.

## Source lineage

The work acknowledges Nick Montfort’s *Taroko Gorge* and links to the Electronic Literature Collection presentation:

https://collection.eliterature.org/3/works/taroko-gorge/taroko-gorge.html

Its dramatic ground is Mohammad Zare’s original play *Grave*.

## Repository boundary

This repository contains only the public runtime and its public documentation. It must not contain the private editing workbook, editable `.taroke.json` projects, diagnostic reports, working-package ZIPs, or private generation materials.

## Citation

See `CITATION.cff`, or cite:

> Zare, Mohammad. *Grave-Machine: An Iranian Remix of Taroko Gorge*. Bilingual generative electronic poem, version 1.1.0, 2026. https://theblackbirdfield.com/works/grave-machine/run/

## Rights

Copyright © 2026 Mohammad Zare. Public source visibility permits reading, linking, study, review, citation, and archival inspection. It does not grant a general license to reproduce, adapt, redistribute, publish, perform, exhibit, commercially use, or train models on the work. See `RIGHTS.md` and `NOTICE.md`.
