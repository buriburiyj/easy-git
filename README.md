<div align="center">

# ✦ Easy Git

**터미널에서 Git을 가장 쉽고 예쁘게**

화살표 키로 움직이고, 엔터로 선택하는 인터랙티브 Git 도구
한국어 친화 · macOS 전용 · 의존성 0

[![macOS](https://img.shields.io/badge/macOS-000000?style=flat-square&logo=apple&logoColor=white)](https://www.apple.com/macos)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-00D9FF?style=flat-square)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/Dependencies-0-00E676?style=flat-square)]()

**🇰🇷 한국어**  ·  [🇺🇸 English](README.en.md)

[설치](#-설치) · [사용법](#-사용법) · [기능](#-기능) · [단축키](#-단축키) · [구조](#-프로젝트-구조)

</div>

<br>

## ✨ 왜 Easy Git 인가요?

매일 반복하는 `git add` → `git commit` → `git push` 가 귀찮으셨나요?
GUI는 무겁고, CLI는 외우기 힘들고, 그 사이 어딘가가 필요했어요.

```bash
# Before
$ git status
$ git add src/App.tsx src/utils/helper.ts README.md
$ git commit -m "✨ feat: 헬퍼 함수 추가"
$ git push

# After
$ gitup
# → 화살표 키로 파일 선택 → 엔터 → 끝
```

<br>

## 📸 미리보기

```
  ✦  Easy Git  ·  my-app
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ●  branch     main
  ●  remote     github.com:me/my-app
  ●  status     5 changed   ·   2 unpushed


  WORKFLOW

  →  🚀  업로드              add · commit · push
     👀  미리보기            colored diff
     ⬇   가져오기            pull from remote
     📜  커밋 기록           recent commits


  BRANCH

     🌿  브랜치              switch · merge · delete
     📦  임시저장            stash
     ↩   되돌리기            reset · revert
     ⚔   충돌 해결           merge conflict


  TOOLS

     🔗  원격 저장소         configure remote
     🚫  .gitignore          templates
     📊  통계                contributors · activity
     💾  백업                zip archive


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↑↓  이동      ↵  선택      1-9  단축      q  종료
```

<details>
<summary><b>📦 파일 선택 화면 보기</b></summary>

```
  ✦  Easy Git  ·  Upload
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  업로드할 파일을 선택하세요


     ●   src/App.tsx                       M    2.3K
  →  ●   src/components/Header.tsx         M    1.1K
     ○   src/utils/helper.ts               A     524
     ●   src/old.js                        D       —
     ○   README.md                         M    3.8K


  3 / 5  selected

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  space  토글     a  전체     ↵  다음     q  뒤로
```

</details>

<details>
<summary><b>💬 커밋 타입 선택 보기</b></summary>

```
  ✦  Easy Git  ·  Commit type
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  커밋 타입을 선택하세요


  →  ✨  feat            새 기능 추가
     🐛  fix             버그 수정
     📝  docs            문서 업데이트
     ♻   refactor        리팩토링
     🎨  style           코드 스타일
     ⚡  perf            성능 개선
     ✅  test            테스트
     🔧  chore           설정 · 빌드

     ✏   custom          직접 입력


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↑↓  이동      ↵  선택      q  뒤로
```

</details>

<details>
<summary><b>📊 통계 화면 보기</b></summary>

```
  ✦  Easy Git  ·  Stats
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


       247                 89                 3
       commits             files              authors



  CONTRIBUTORS

  민수      ████████████████████        180
  지은      ██████                       52
  서준      █▎                           15


  ACTIVITY     last 30 days

  ▂▃▅█▇▆▄▃▂  ▁▂▃▅▆█▇▅▃▂▁  ▃▅▇█▆▄▂


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↵  뒤로
```

</details>

<br>

## 🚀 설치

### 한 줄 설치 (권장)

```bash
curl -fsSL https://raw.githubusercontent.com/USERNAME/easy-git/main/install.sh | bash
```

### 수동 설치

```bash
git clone https://github.com/USERNAME/easy-git.git
cd easy-git
chmod +x install.sh
./install.sh
```

설치 후 어느 폴더에서든 `gitup` 명령으로 실행됩니다.

### 요구사항

| 항목 | 버전 | 비고 |
|:---|:---|:---|
| macOS | 10.14+ | |
| Python | 3.8+ | macOS 기본 탑재 |
| Git | 2.0+ | `brew install git` |

> **추가 라이브러리 설치 필요 없음** — Python 표준 라이브러리만 사용합니다.

<br>

## 📖 사용법

### 기본 사용

프로젝트 폴더로 이동해서 `gitup` 만 입력하면 끝입니다.

```bash
cd ~/projects/my-app
gitup
```

처음 실행하면 저장소 선택 화면이 뜨고, 한 번 사용한 폴더는 자동으로 기억됩니다.

<br>

### 시나리오 1 · 매일 쓰는 업로드 플로우

```
1.  gitup 실행
        ↓
2.  메인 메뉴에서 "🚀 업로드" 선택  →  Enter
        ↓
3.  파일 목록에서 원하는 파일 체크  →  Space (다중 선택)
        ↓
4.  Enter로 다음 단계
        ↓
5.  커밋 타입 선택  →  feat / fix / docs ...
        ↓
6.  상세 설명 입력  →  Enter
        ↓
7.  확인 화면에서 "진행" 선택  →  Enter
        ↓
8.  ✓ add  →  ✓ commit  →  ✓ push  →  🎉 완료
```

**팁** — 모든 파일을 한 번에 올리려면 파일 선택 화면에서 <kbd>A</kbd> 누르면 전체 선택됩니다.

<br>

### 시나리오 2 · 처음 GitHub에 올리기

```bash
cd ~/projects/new-project
gitup

# 1. "Git 저장소가 아닙니다" 안내 →  "git init 할까요?" 에서 Y
# 2. 메인 메뉴 →  🔗 원격 저장소  →  ➕ origin 추가
# 3. URL 입력 (예: git@github.com:USERNAME/new-project.git)
# 4. 메인 메뉴로 복귀 →  🚀 업로드 →  파일 전체 선택
# 5. 첫 커밋 메시지 작성 후 push
```

<br>

### 시나리오 3 · 실수로 한 커밋 되돌리기

```
메인 메뉴  →  ↩  되돌리기

  →  📌  마지막 커밋 취소       keep changes      ← 작업 내용은 살림
     💥  마지막 커밋 삭제       discard all
     📄  파일 변경 되돌리기     checkout files
     ✏   커밋 메시지 수정       amend message     ← 메시지만 수정
```

- **메시지만 바꾸고 싶다면** → "커밋 메시지 수정"
- **파일을 더 추가하고 다시 커밋하려면** → "마지막 커밋 취소"
- **완전히 없던 일로 하고 싶다면** → "마지막 커밋 삭제" (⚠ 주의)

<br>

### 시나리오 4 · 작업 중 다른 일이 생겼을 때

```
메인 메뉴  →  📦  임시저장  →  💾 현재 저장

(다른 작업 수행)

메인 메뉴  →  📦  임시저장  →  📥 복원
```

<br>

### 시나리오 5 · pull 했더니 충돌

```
메인 메뉴  →  ⚔  충돌 해결

  →  📝  에디터로 열기       VS Code에서 직접 수정
     ⬅   내 버전 적용        내 코드 유지
     ➡   상대 버전 적용      원격 코드 채택
     ✋  병합 중단           아예 취소
     ✅  해결 완료           수정 후 커밋
```

<br>

### 시나리오 6 · .gitignore 추가

```
메인 메뉴  →  🚫  .gitignore

  사용할 템플릿을 선택하세요 (복수 선택)

     ●   Python
     ●   Node.js
     ●   macOS

  Space 체크  →  Enter 생성  →  .gitignore 자동 작성
```

<br>

## ⚡ 기능

<table>
<tr>
<td width="50%" valign="top">

### 🚀 Workflow

- **업로드** — 파일 체크박스 선택 후 add · commit · push 한 번에
- **미리보기** — 색상 입힌 diff로 변경사항 확인
- **가져오기** — 원격에서 pull
- **커밋 기록** — 최근 커밋을 보기 좋게

### 🌿 Branch & State

- **브랜치** — 전환 · 생성 · 병합 · 삭제 · 이름변경
- **임시저장** — stash save / pop / show
- **되돌리기** — 커밋 취소, 파일 복원, 메시지 수정
- **충돌 해결** — merge conflict 가이드

</td>
<td width="50%" valign="top">

### 🛠 Tools

- **원격 저장소** — origin 추가 / 변경 / 삭제
- **.gitignore** — Python · Node · macOS 등 템플릿
- **통계** — 기여자 · 활동량 시각화
- **백업** — 프로젝트 zip 압축

### ✨ UX

- **화살표 키 인터랙티브** — 마우스 클릭 같은 직관성
- **체크리스트 선택** — 스페이스로 토글
- **컨벤셔널 커밋** — 8가지 타입 템플릿
- **언제든 `q`** — 어디서든 메뉴로 즉시 복귀

</td>
</tr>
</table>

<br>

## ⌨️ 단축키

| 키 | 동작 |
|:---:|:---|
| <kbd>↑</kbd> <kbd>↓</kbd> | 항목 이동 |
| <kbd>←</kbd> <kbd>→</kbd> | 좌우 토글 (예/아니오) |
| <kbd>Enter</kbd> | 선택 / 확정 |
| <kbd>Space</kbd> | 체크박스 토글 |
| <kbd>A</kbd> | 전체 선택 / 해제 |
| <kbd>1</kbd> - <kbd>9</kbd> | 메뉴 번호 단축키 |
| <kbd>Y</kbd> / <kbd>N</kbd> | 예 / 아니오 단축 |
| <kbd>Q</kbd> / <kbd>Esc</kbd> | 뒤로 / 메인 메뉴 |
| <kbd>Ctrl</kbd> + <kbd>C</kbd> | 전체 종료 |

<br>

## 📂 프로젝트 구조

```
easy-git/
│
├── 📄 easy_git.py                  ← 실행 진입점
├── 📄 install.sh                   ← macOS 설치 스크립트
├── 📄 README.md                    ← 프로젝트 소개 (한국어)
├── 📄 README.en.md                 ← Project intro (English)
├── 📄 LICENSE                      ← MIT 라이선스
├── 📄 .gitignore
│
└── 📁 egp/                         ← 메인 패키지
    │
    ├── 📄 __init__.py
    ├── 📄 config.py                ← 설정 파일 관리
    ├── 📄 ui.py                    ← UI · 색상 · 박스 렌더링
    ├── 📄 keys.py                  ← 키보드 입력 처리
    ├── 📄 git_core.py              ← Git 명령 래퍼
    ├── 📄 menu.py                  ← 메인 메뉴 라우터
    │
    └── 📁 features/                ← 기능별 모듈
        │
        ├── 📄 __init__.py
        ├── 📄 upload.py            ← 🚀 업로드
        ├── 📄 diff_view.py         ← 👀 변경 미리보기
        ├── 📄 branch.py            ← 🌿 브랜치 관리
        ├── 📄 stash.py             ← 📦 임시저장
        ├── 📄 undo.py              ← ↩  되돌리기
        ├── 📄 log_view.py          ← 📜 커밋 기록
        ├── 📄 remote.py            ← 🔗 원격 저장소
        ├── 📄 conflict.py          ← ⚔  충돌 해결
        ├── 📄 gitignore.py         ← 🚫 .gitignore 생성
        ├── 📄 stats.py             ← 📊 통계
        └── 📄 backup.py            ← 💾 백업 zip
```

### 모듈별 책임

| 모듈 | 역할 |
|:---|:---|
| `easy_git.py` | 앱 시작점. `egp.menu.run_app()` 호출 |
| `egp/config.py` | 최근 저장소 목록을 `~/.easy_git_config.json`에 저장 |
| `egp/ui.py` | 헤더 · 박스 · 메뉴 · 체크리스트 · 다이얼로그 렌더링 |
| `egp/keys.py` | 화살표 · 엔터 · 스페이스 등 raw 키 입력 |
| `egp/git_core.py` | `subprocess`로 git 명령 실행 · 결과 파싱 |
| `egp/menu.py` | 메인 메뉴 출력 · 기능 라우팅 · `q` 복귀 처리 |
| `egp/features/*` | 각 기능 화면 · 흐름 구현 |

<br>

## 🎨 디자인 철학

**미니멀** — 박스로 모든 걸 감싸지 않습니다. 정말 필요한 곳에만 선을 긋습니다.
**일관성** — 모든 페이지가 같은 헤더 · 같은 푸터 · 같은 키 힌트 형식입니다.
**친근함** — 한글 라벨이 메인, 영문은 부가설명. 둘 다 익숙합니다.
**절제** — 색상 6가지, 이모지는 메뉴 항목당 하나, 여백은 충분히.

<br>

## 🗺 로드맵

- [x] 인터랙티브 화살표 키 UI
- [x] 파일 체크리스트 선택
- [x] 컨벤셔널 커밋 템플릿
- [x] 브랜치 · stash · 되돌리기
- [x] 충돌 해결 도우미
- [x] .gitignore 템플릿
- [x] 통계 시각화
- [x] 한국어 · 영어 README
- [ ] GitHub CLI (`gh`) 연동 — PR 생성
- [ ] 앱 내 다국어 지원 (현재는 한국어만)
- [ ] 테마 (Slate / Neon / Mono)
- [ ] Linux 지원

<br>

## ❓ FAQ

<details>
<summary><b>Q. 기존 git 명령어와 같이 써도 되나요?</b></summary>

네, 전혀 문제 없습니다. Easy Git은 내부적으로 표준 git 명령을 실행할 뿐이라 어떤 상태도 변형하지 않습니다.

</details>

<details>
<summary><b>Q. push할 때 인증은 어떻게 하나요?</b></summary>

기존에 설정해둔 SSH 키 또는 macOS 키체인의 자격증명을 그대로 사용합니다. Easy Git이 별도로 묻지 않습니다.

</details>

<details>
<summary><b>Q. 설정 파일은 어디 있나요?</b></summary>

`~/.easy_git_config.json` 에 저장됩니다. 최근 사용한 저장소 목록 정도만 들어있어요.

</details>

<details>
<summary><b>Q. 제거하려면요?</b></summary>

```bash
rm -rf ~/.easy-git
rm /usr/local/bin/gitup
rm ~/.easy_git_config.json
```

</details>

<br>

## 🛠 개발

```bash
git clone https://github.com/USERNAME/easy-git.git
cd easy-git
python3 easy_git.py
```

새 기능을 추가하려면 `egp/features/` 아래에 모듈을 만들고, `egp/menu.py`의 `ACTIONS` 딕셔너리에 등록하면 됩니다.

<br>

## 🤝 기여

이슈와 PR 환영합니다. 큰 변경은 먼저 이슈로 논의해주세요.

<br>

## 📜 라이선스

[MIT](LICENSE) © 2026

<br>

## 💌 만든 이유

```
git add .
git commit -m "변경 내용 설명"
git push
```

이 세 줄을 매일 수십 번 치면서, "더 쉬울 수 없을까?" 생각하다 만들었습니다.
마우스 클릭처럼 직관적이고, GUI 도구처럼 예쁘면서, 터미널의 가벼움은 그대로.

당신의 Git 라이프가 조금 더 즐거워지길 바라며.

<br>

<div align="center">

**터미널에서, 더 쉽게, 더 예쁘게**

⭐ 마음에 드셨다면 Star 부탁드려요

</div>
