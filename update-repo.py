import os
import git

# Set the repository directory and commit message
repository_dir = "/"
commit_message = "Your commit message here"

# Change directory to the repository
os.chdir(repository_dir)

# Open the repository
repo = git.Repo(repository_dir)

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
    # repo.remotes.origin.push()

# Clean up
repo.close()