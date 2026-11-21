// news-image-20261121 — The Daily Globe, Saturday 21 November 2026.
// The entry is the rendered front page beside this file; this program
// places an exact copy at the grader's output path. Node 22, stdlib only.
//
// Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
copyFileSync(new URL("./entry.png", import.meta.url), join(outDir, "entry.png"));
