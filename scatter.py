from github import Github
import matplotlib.pyplot as plt
import numpy as np

# GitHub
github_username = "username"
github_access_token = "github_api"

# GitHub API
if github_access_token:
    g = Github(github_access_token)
else:
    g = Github()

user = g.get_user(github_username)
repos = user.get_repos()
activities = [repo.get_commits() for repo in repos]
#scatter
activity_dates = []
for commits in activities:
    for commit in commits.get_page(0):
        activity_dates.append(commit.commit.author.date)

activity_dates = sorted(activity_dates)
activity_counts = [activity_dates.count(date) for date in activity_dates]

activity_x = range(len(activity_dates))
activity_y = activity_counts

fig, ax = plt.subplots()
ax.scatter(activity_x, activity_y, s=10, c=activity_dates, cmap="viridis")
ax.set_title(f"GitHub Activity - {github_username}")
ax.set_xlabel("Activity Count")
ax.set_ylabel("Date")
cbar = ax.figure.colorbar(ax.collections[0])
cbar.ax.set_ylabel("Date", rotation=-90, va="bottom")
plt.tight_layout()
plt.savefig("github_activity_scatter.png", dpi=300, bbox_inches="tight")
plt.show()