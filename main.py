from github import Github
import matplotlib.pyplot as plt
import numpy as np

# GitHub
github_username = "username"
github_access_token = "github_api"
if github_access_token:
    g = Github(github_access_token)
else:
    g = Github()
user = g.get_user(github_username)
repos = user.get_repos()
activities = [repo.get_commits() for repo in repos]

# Counter
activity_counts = {
    "Repositories": len(repos),
    "Commits": sum([len(commits.get_page(0)) for commits in activities]),
    "Forks": sum([repo.forks_count for repo in repos]),
    "Pull Requests": sum([repo.open_issues_count for repo in repos]),
    "Stars": sum([repo.stargazers_count for repo in repos]),
}

colors = plt.cm.Paired(range(len(activity_counts)))
explode = (0.1, 0, 0, 0, 0) 
plt.style.use("seaborn-darkgrid")

labels = list(activity_counts.keys())
sizes = list(activity_counts.values())

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", shadow=True, startangle=140)
ax.axis("equal")
ax.set_title(f"GitHub Summary - {github_username}", fontsize=16, fontweight="bold", color="#333333")
for text in ax.texts:
    text.set_fontsize(12)
    text.set_color("white")
plt.tight_layout()
plt.savefig("github_activity_pie.png", dpi=300, bbox_inches="tight")
plt.show()
activity_dates = []
for commits in activities:
    for commit in commits.get_page(0):
        activity_dates.append(commit.commit.author.date)

activity_dates = sorted(activity_dates)
activity_counts = [activity_dates.count(date) for date in activity_dates]
fig, ax = plt.subplots()
ax.plot(activity_dates, activity_counts)
ax.set_title(f"GitHub Activity - {github_username}")
ax.set_xlabel("Date")
ax.set_ylabel("Activity Count")
ax.grid(axis="both", linestyle="--", color="gray", alpha=0.5)
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("github_activity_timeline.png", dpi=300, bbox_inches="tight")
plt.show()
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