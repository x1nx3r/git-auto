import os
import git

script_dir = os.path.dirname(os.path.realpath(__file__))

# Change directory to the repository
os.chdir(script_dir)
repository_dir = script_dir

commit_message = "Your commit message here"

# Open the repository
repo = git.Repo(repository_dir)

# Iterate through all files in the repository, including those in subdirectories
for root, _, files in os.walk(repository_dir):
    for file in files:
        file_path = os.path.join(root, file)

        # Check if the file is untracked
        if file_path not in repo.untracked_files:
            if repo.is_dirty(path=file_path):
                repo.git.add(file_path)

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
