<div align="center">

# ✦ Easy Git

**The easiest and prettiest way to use Git in the terminal**

An interactive Git tool with arrow-key navigation and Enter to select
macOS only · Zero dependencies

[![macOS](https://img.shields.io/badge/macOS-000000?style=flat-square&logo=apple&logoColor=white)](https://www.apple.com/macos)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-00D9FF?style=flat-square)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/Dependencies-0-00E676?style=flat-square)]()

[🇰🇷 한국어](README.md)  ·  **🇺🇸 English**

[Install](#-installation) · [Usage](#-usage) · [Features](#-features) · [Shortcuts](#%EF%B8%8F-shortcuts) · [Structure](#-project-structure)

</div>

<br>

## ✨ Why Easy Git?

Tired of typing `git add` → `git commit` → `git push` every day?
GUIs are heavy, CLIs are hard to memorize, you needed something in between.

```bash
# Before
$ git status
$ git add src/App.tsx src/utils/helper.ts README.md
$ git commit -m "✨ feat: add helper function"
$ git push

# After
$ gitup
# → Pick files with arrow keys → Enter → Done
```

<br>

## 📸 Preview

```
  ✦  Easy Git  ·  my-app
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ●  branch     main
  ●  remote     github.com:me/my-app
  ●  status     5 changed   ·   2 unpushed


  WORKFLOW

  →  🚀  Upload              add · commit · push
     👀  Preview             colored diff
     ⬇   Pull                fetch from remote
     📜  History             recent commits


  BRANCH

     🌿  Branch              switch · merge · delete
     📦  Stash               temporary save
     ↩   Undo                reset · revert
     ⚔   Conflicts           merge conflict


  TOOLS

     🔗  Remote              configure remote
     🚫  .gitignore          templates
     📊  Stats               contributors · activity
     💾  Backup              zip archive


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↑↓  navigate     ↵  select     1-9  hotkeys     q  quit
```

<details>
<summary><b>📦 File picker screen</b></summary>

```
  ✦  Easy Git  ·  Upload
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Select files to commit


     ●   src/App.tsx                       M    2.3K
  →  ●   src/components/Header.tsx         M    1.1K
     ○   src/utils/helper.ts               A     524
     ●   src/old.js                        D       —
     ○   README.md                         M    3.8K


  3 / 5  selected

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  space  toggle     a  all     ↵  next     q  back
```

</details>

<details>
<summary><b>💬 Commit type picker</b></summary>

```
  ✦  Easy Git  ·  Commit type
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Select a commit type


  →  ✨  feat            new feature
     🐛  fix             bug fix
     📝  docs            documentation
     ♻   refactor        code refactor
     🎨  style           formatting
     ⚡  perf            performance
     ✅  test            tests
     🔧  chore           config · build

     ✏   custom          write your own


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↑↓  navigate     ↵  select     q  back
```

</details>

<details>
<summary><b>📊 Stats screen</b></summary>

```
  ✦  Easy Git  ·  Stats
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


       247                 89                 3
       commits             files              authors



  CONTRIBUTORS

  Minsu     ████████████████████        180
  Jieun     ██████                       52
  Seojun    █▎                           15


  ACTIVITY     last 30 days

  ▂▃▅█▇▆▄▃▂  ▁▂▃▅▆█▇▅▃▂▁  ▃▅▇█▆▄▂


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↵  back
```

</details>

<br>

## 🚀 Installation

### One-line install (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/buriburiyj/easy-git/main/install.sh | bash
```

### Manual install

```bash
git clone https://github.com/buriburiyj/easy-git.git
cd easy-git
chmod +x install.sh
./install.sh
```

After installation, run `gitup` from any directory.

### Requirements

| Tool | Version | Note |
|:---|:---|:---|
| macOS | 10.14+ | |
| Python | 3.8+ | Comes with macOS |
| Git | 2.0+ | `brew install git` |

> **No extra libraries needed** — Uses only Python standard library.

<br>

## 📖 Usage

### Basic

Navigate to your project folder and just run `gitup`.

```bash
cd ~/projects/my-app
gitup
```

The first run shows a repo picker, and used folders are remembered automatically.

<br>

### Scenario 1 · Daily upload flow

```
1.  Run gitup
        ↓
2.  Select "🚀 Upload" from main menu  →  Enter
        ↓
3.  Check files you want to commit  →  Space (multi-select)
        ↓
4.  Enter to proceed
        ↓
5.  Pick commit type  →  feat / fix / docs ...
        ↓
6.  Type details  →  Enter
        ↓
7.  Confirm with "Proceed"  →  Enter
        ↓
8.  ✓ add  →  ✓ commit  →  ✓ push  →  🎉 Done
```

**Tip** — Press <kbd>A</kbd> on the file picker to select all at once.

<br>

### Scenario 2 · First push to GitHub

```bash
cd ~/projects/new-project
gitup

# 1. "Not a git repo" prompt →  "Run git init?" →  Y
# 2. Main menu →  🔗 Remote  →  ➕ Add origin
# 3. Enter URL (e.g. git@github.com:USERNAME/new-project.git)
# 4. Back to main →  🚀 Upload →  Select all files
# 5. Write first commit message and push
```

<br>

### Scenario 3 · Undo a mistake

```
Main menu  →  ↩  Undo

  →  📌  Cancel last commit       keep changes      ← keeps your work
     💥  Discard last commit      delete everything
     📄  Revert file changes      checkout files
     ✏   Amend commit message     edit message only
```

- **Change message only** → "Amend commit message"
- **Add more files and recommit** → "Cancel last commit"
- **Throw it all away** → "Discard last commit" (⚠ careful)

<br>

### Scenario 4 · Interrupt your work

```
Main menu  →  📦  Stash  →  💾 Save current

(do other work)

Main menu  →  📦  Stash  →  📥 Pop
```

<br>

### Scenario 5 · Pull caused conflicts

```
Main menu  →  ⚔  Conflicts

  →  📝  Open in editor       open in VS Code
     ⬅   Use ours             keep mine
     ➡   Use theirs           accept incoming
     ✋  Abort merge          cancel everything
     ✅  Mark resolved        commit fixes
```

<br>

### Scenario 6 · Add .gitignore

```
Main menu  →  🚫  .gitignore

  Pick templates (multi-select)

     ●   Python
     ●   Node.js
     ●   macOS

  Space to check  →  Enter to generate
```

<br>

## ⚡ Features

<table>
<tr>
<td width="50%" valign="top">

### 🚀 Workflow

- **Upload** — Pick files with checkboxes, then add · commit · push in one go
- **Preview** — View changes with colored diff
- **Pull** — Fetch from remote
- **History** — Browse recent commits

### 🌿 Branch & State

- **Branch** — Switch · create · merge · delete · rename
- **Stash** — save / pop / show
- **Undo** — Cancel commits, restore files, edit messages
- **Conflicts** — Merge conflict helper

</td>
<td width="50%" valign="top">

### 🛠 Tools

- **Remote** — Add / change / remove origin
- **.gitignore** — Python · Node · macOS templates
- **Stats** — Contributors · activity charts
- **Backup** — Zip the project

### ✨ UX

- **Arrow-key interactive** — Feels like clicking
- **Checklist select** — Toggle with Space
- **Conventional commits** — 8 type templates built in
- **Press `q` anytime** — Jump back to main menu instantly

</td>
</tr>
</table>

<br>

## ⌨️ Shortcuts

| Key | Action |
|:---:|:---|
| <kbd>↑</kbd> <kbd>↓</kbd> | Navigate items |
| <kbd>←</kbd> <kbd>→</kbd> | Toggle yes/no |
| <kbd>Enter</kbd> | Select / confirm |
| <kbd>Space</kbd> | Toggle checkbox |
| <kbd>A</kbd> | Select / deselect all |
| <kbd>1</kbd> - <kbd>9</kbd> | Menu hotkey |
| <kbd>Y</kbd> / <kbd>N</kbd> | Yes / No shortcut |
| <kbd>Q</kbd> / <kbd>Esc</kbd> | Back / main menu |
| <kbd>Ctrl</kbd> + <kbd>C</kbd> | Quit entirely |

<br>

## 📂 Project Structure

```
easy-git/
│
├── 📄 easy_git.py                  ← Entry point
├── 📄 install.sh                   ← macOS install script
├── 📄 README.md                    ← Project intro (Korean)
├── 📄 README.en.md                 ← Project intro (English)
├── 📄 LICENSE                      ← MIT license
├── 📄 .gitignore
│
└── 📁 egp/                         ← Main package
    │
    ├── 📄 __init__.py
    ├── 📄 config.py                ← Config file management
    ├── 📄 ui.py                    ← UI · colors · box rendering
    ├── 📄 keys.py                  ← Keyboard input
    ├── 📄 git_core.py              ← Git command wrapper
    ├── 📄 menu.py                  ← Main menu router
    │
    └── 📁 features/                ← Feature modules
        │
        ├── 📄 __init__.py
        ├── 📄 upload.py            ← 🚀 Upload
        ├── 📄 diff_view.py         ← 👀 Preview
        ├── 📄 branch.py            ← 🌿 Branch
        ├── 📄 stash.py             ← 📦 Stash
        ├── 📄 undo.py              ← ↩  Undo
        ├── 📄 log_view.py          ← 📜 History
        ├── 📄 remote.py            ← 🔗 Remote
        ├── 📄 conflict.py          ← ⚔  Conflicts
        ├── 📄 gitignore.py         ← 🚫 .gitignore
        ├── 📄 stats.py             ← 📊 Stats
        └── 📄 backup.py            ← 💾 Backup
```

### Module responsibilities

| Module | Role |
|:---|:---|
| `easy_git.py` | App entry. Calls `egp.menu.run_app()` |
| `egp/config.py` | Stores recent repos in `~/.easy_git_config.json` |
| `egp/ui.py` | Renders headers · boxes · menus · checklists · dialogs |
| `egp/keys.py` | Raw key input — arrows, enter, space (uses termios) |
| `egp/git_core.py` | Runs git via `subprocess` and parses output |
| `egp/menu.py` | Main menu · routing · `q` back-handler |
| `egp/features/*` | Each feature screen and its flow |

<br>

## 🎨 Design Philosophy

**Minimal** — No box around every single thing. Only where it really helps.
**Consistent** — Every page shares the same header · footer · key-hint format.
**Friendly** — Clear labels with helpful descriptions, never overwhelming.
**Restrained** — 6 colors, one emoji per menu item, plenty of whitespace.

<br>

## 🗺 Roadmap

- [x] Arrow-key interactive UI
- [x] File checklist selection
- [x] Conventional commit templates
- [x] Branch · stash · undo
- [x] Merge conflict helper
- [x] .gitignore templates
- [x] Stats visualization
- [x] Korean · English README
- [ ] GitHub CLI (`gh`) integration — create PRs
- [ ] In-app i18n (Korean only for now)
- [ ] Themes (Slate / Neon / Mono)
- [ ] Linux support

<br>

## ❓ FAQ

<details>
<summary><b>Q. Can I still use plain git commands alongside?</b></summary>

Absolutely. Easy Git just wraps the standard git binary — it never alters your repository state in unusual ways.

</details>

<details>
<summary><b>Q. How does authentication work for push?</b></summary>

It uses whatever you have already configured — SSH keys or macOS keychain credentials. Easy Git never prompts for credentials.

</details>

<details>
<summary><b>Q. Where is the config file?</b></summary>

`~/.easy_git_config.json`. It only contains your recent repo list.

</details>

<details>
<summary><b>Q. How do I uninstall?</b></summary>

```bash
rm -rf ~/.easy-git
rm /usr/local/bin/gitup
rm ~/.easy_git_config.json
```

</details>

<br>

## 🛠 Development

```bash
git clone https://github.com/USERNAME/easy-git.git
cd easy-git
python3 easy_git.py
```

To add a new feature, drop a module under `egp/features/` and register it in the `ACTIONS` dict in `egp/menu.py`.

<br>

## 🤝 Contributing

Issues and PRs are welcome. Please open an issue first to discuss any large changes.

<br>

## 📜 License

[MIT](LICENSE) © 2026

<br>

## 💌 Why I Built This

```
git add .
git commit -m "update"
git push
```

After typing these three lines hundreds of times, I kept thinking: "Can't this be easier?"
As intuitive as a mouse click, as pretty as a GUI tool, but as lightweight as a terminal.

Hope your Git life feels a little more joyful.

<br>

<div align="center">

**Easier and prettier — right in your terminal**

⭐ Star the repo if you like it

</div>
