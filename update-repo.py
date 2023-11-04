import os
from git import Repo, cmd

script_dir = os.path.dirname(os.path.realpath(__file__))

# Change directory to the repository
os.chdir(script_dir)
repository_dir = script_dir

commit_message = "Your commit message here"

# Open the repository
repo = Repo(repository_dir)

# Use the git.cmd.Git class to execute 'git add' recursively
git = cmd.Git(repository_dir)
git.execute(['git', 'add', '.'])

# Check if there are any changes
if not repo.is_dirty():
    print("No changes to commit.")
else:
    # Commit the changes with the provided commit message
    repo.index.commit(commit_message)
    print("Changes committed successfully.")

    # Push the committed changes to the remote repository
    origin = repo.remote(name='origin')
    origin.push()

# Clean up
repo.close()