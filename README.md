# fortune-teller
# 🔮 GitHub Actions Practice - Commit Fortune Teller

Welcome to your first GitHub Actions project! This application generates a fun fortune prediction every time you commit code.

## What You'll Learn
- ✅ How workflows are triggered by Git events
- ✅ Setting up Python environments
- ✅ Running tests automatically
- ✅ Using environment variables
- ✅ Creating workflow artifacts
- ✅ Adding PR comments
- ✅ Viewing workflow logs

## How It Works
1. Make a code change and commit it
2. GitHub Actions automatically runs:
   - Sets up Python
   - Installs dependencies
   - Runs tests
   - Generates your fortune
3. Results:
   - Downloadable text file with your fortune
   - Comment on your PR (if applicable)
   - Fortune printed in workflow logs

## Getting Started
1. Fork this repository
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/fortune-teller.git`
3. Make a small change and commit it
4. Watch the magic happen in the Actions tab!

## Learning Challenges
1. Add a new fortune to the list in `fortune_teller.py`
2. Modify the workflow to run only on push to main
3. Add a step that saves fortunes to a file named with the commit SHA