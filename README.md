# MyJobMatch Analyze

A Claude Code plugin that scores how well your resume matches a job
description - straight from your terminal, using the same rubric as
[MyJobMatch.ai](https://myjobmatch.ai/)'s Analyze feature.

Give it a resume (pasted text, or a `.docx`/`.pdf`/plain text file path) and
a job description (pasted text, a file, or a job posting URL), and it
returns:

- A 0-100 fit score
- Concrete strengths tied to specifics in your resume
- Concrete gaps relative to the job description
- Two interview talking points to help you close a gap or lean into a
  strength

No API key, no account, no cost beyond the conversation you're already
having - the analysis runs entirely in your Claude Code session. `.docx`
parsing is done by a small bundled script using only Python's standard
library (`scripts/extract_docx_text.py`) - no `python-docx`/`lxml` install
required, just a `python3` or `python` on your PATH.

## Install

```bash
# from a local checkout, while developing/testing
claude --plugin-dir ./myjobmatch-analyzer
```

From this repo directly:

```
/plugin marketplace add powellbj/myjobmatch-analyzer
/plugin install myjobmatch-analyzer
```

or, in the desktop app, Settings → Plugins → Add, and point it at this repo.

## Use

```
/myjobmatch-analyzer:analyze
```

or just ask in conversation - e.g. "does my resume match this job posting?"
with a resume and a job description (or link) at hand. The skill's
description is written so Claude can pick it up automatically in that case
too.

## Why only two talking points?

This plugin is intentionally a smaller slice of MyJobMatch.ai's full
Analyze feature - a useful one-shot check, not a replacement for the
hosted app, which also saves your analysis history, generates a tailored
resume and cover letter for the job, and tracks the application end to end.

## License

MIT - see [LICENSE](LICENSE).
