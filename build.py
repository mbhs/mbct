from staticjinja import Site
import json

if __name__ == "__main__":
    # load in news posts - temporarily before moving to non-static server?
    f = open("news_posts.json")
    posts = json.loads(f.read())
    f.close()
    # news context
    news_context = {"posts":posts}

    site = Site.make_site(contexts=[("news.html",news_context)],searchpath="templates",outpath="output")

    # enable automatic reloading
    site.render()