from staticjinja import Site
import json
from urllib.parse import urlparse

if __name__ == "__main__":
    # load in news posts - temporarily before moving to non-static server?
    f = open("news_posts.json")
    posts = json.loads(f.read())
    f.close()
    
    # load in curriculum problems - temporarily before moving to non-static server?
    f = open("problems.json")
    problems = json.loads(f.read())
    f.close()
    
    # some processing of the problems
    for itemSet in problems:
        for item in itemSet["items"]:
            if item['type'] == "problem":
                if "usaco.org" in item["url"]:
                    item["source"] = "USACO"
                elif "atcoder.jp" in item["url"]:
                    item["source"] = "AtCoder"
                elif "cses.fi" in item["url"]:
                    item["source"] = "CSES"
                elif "codechef.com" in item["url"]:
                    item["source"] = "Codechef"
                elif "codeforces" in item["url"]:
                    item["source"] = "Codeforces"
                elif "szkopul.edu.pl" in item["url"]:
                    item["source"] = "SZKOPUL"
                elif "customSource" in item:
                    item["source"] = item["customSource"]
                else:
                    item["source"] = "Other"

    # news context
    news_context = {"posts":posts}
    # curriculum context
    curriculum_context = {"meeting_problems":problems}

    # generate site files
    site = Site.make_site(contexts=[("news.html",news_context),("curriculum.html",curriculum_context)],searchpath="templates",outpath="output")

    # enable automatic reloading
    site.render()