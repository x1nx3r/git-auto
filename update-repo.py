import os
import git

# Set the repository directory and commit message
commit_message = "Your commit message here"

script_dir = os.path.dirname(os.path.realpath(__file__))

# Change directory to the repository
os.chdir(script_dir)

# Open the repository
repo = git.Repo(script_dir)

# Check if there are any changes
if not repo.is_dirty():
    print("No changes to commit.")
else:
    # Stage all changes (including untracked files)
    repo.git.add(A=True)

    # Commit the changes with the provided commit message
    repo.index.commit(commit_message)
    print("Changes committed successfully.")

    # Push to the remote repository (if needed)
    repo.remotes.origin.push()
    print("Changes pushed successfully.")

# Clean up
repo.close()