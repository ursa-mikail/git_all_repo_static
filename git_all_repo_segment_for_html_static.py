import requests

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching repositories: {response.status_code}")

def generate_html(repos):
    html = ""
    for repo in repos:
        repo_name = repo['name']
        repo_url = repo['html_url']
        repo_lang = repo['language'] or "Unknown"
        repo_lang_color = get_language_color(repo_lang)

        html += f"""
    <li
      class="mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6"
    >
      <div
        class="Box pinned-item-list-item d-flex p-3 width-full public source"
      >
        <div class="pinned-item-list-item-content">
          <div class="d-flex v-align-middle mr-2">
            <span data-view-component="true" class="position-relative"><a id="{repo['id']}" href="{repo_url}" data-view-component="true" class="min-width-0 Link text-bold flex-auto wb-break-all">
              <span class="repo" >
                {repo_name}
              </span>
</a><tool-tip id="tooltip-{repo['id']}" for="{repo['id']}" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">{repo_name}</tool-tip></span>            <span class="flex-auto text-right">
              <span></span><span class="Label Label--secondary v-align-middle ">Public</span>
            </span>
          </div>

          <p class="pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3">
            
          </p>

          <p class="mb-0 f6 color-fg-muted">
              <span class="d-inline-block mr-3">
  <span class="repo-language-color" style="background-color: {repo_lang_color}"></span>
  <span itemprop="programmingLanguage">{repo_lang}</span>
</span>

          </p>
        </div>
      </div>
    </li>
"""
    return html

def get_language_color(language):
    # This function returns a color based on the language
    # For simplicity, a hard-coded mapping is used
    # You can expand it as needed or fetch from a reliable source
    colors = {
        "Python": "#3572A5",
        "JavaScript": "#f1e05a",
        "Shell": "#89e051",
        "Java": "#b07219",
        "HTML": "#e34c26",
        "CSS": "#563d7c",
        "Unknown": "#cccccc"
    }
    return colors.get(language, "#cccccc")

if __name__ == "__main__":
    username = "ursa-mikail"  # Replace with the GitHub username
    repos = get_repos(username)
    html_output = generate_html(repos)
    print(html_output)
