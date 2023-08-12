from github import Github
import matplotlib.pyplot as plt

# Github
github_username = "username"

# Github API 
github_access_token = "github_api"

# Github 
if github_access_token:
    g = Github(github_access_token)
else:
    g = Github()


user = g.get_user(github_username)
repos = user.get_repos()
activities = [repo.get_commits() for repo in repos]

# Counter
activity_counts = {
    "Commits": sum([len(commits) for commits in activities]),
    "Forks": sum([repo.forks_count for repo in repos]),
    "Pull Requests": sum([repo.open_issues_count for repo in repos]),
    "Stars": sum([repo.stargazers_count for repo in repos]),
}

# Color style
colors = plt.cm.Paired(range(len(activity_counts)))
explode = (0.1, 0, 0, 0)  # Sektörleri dışarı çıkar
plt.style.use("seaborn-darkgrid")

# Draw graphics
labels = list(activity_counts.keys())
sizes = list(activity_counts.values())

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", shadow=True, startangle=140)
ax.axis("equal")
ax.set_title(f"GitHub Summary- {github_username}", fontsize=16, fontweight="bold", color="#333333")

# graphics more style
for text in ax.texts:
    text.set_fontsize(12)
    text.set_color("white")

# Show and save
plt.tight_layout()
plt.savefig("github_activity_pie.png", dpi=300, bbox_inches="tight")
plt.show()
