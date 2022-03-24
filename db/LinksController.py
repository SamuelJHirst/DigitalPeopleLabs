from db.connection import db

class LinksController:
    @staticmethod
    def create_link(name, textColour, backgroundColour, url):
        db.links.insert_one({
            "name": name,
            "textColour": textColour,
            "backgroundColour": backgroundColour,
            "url": url
        })

        return True

    @staticmethod
    def get_all_links():
        links = db.links.find({}, { "_id": 0, "__v": 0 })
        links = links.sort("name")
        links = list(links)

        return links
