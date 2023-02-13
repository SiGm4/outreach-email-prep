import re
from datetime import datetime
import calendar

domain_regex = "^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)"

def molly_email(recipient_name, target_url, topic, our_url, anchor_text, link_exchange):
    paragraphs = []
    paragraphs.append("Hey " + recipient_name + ",")
    paragraphs.append("Dimitris here from the content team at memberstack.com (DR 73).")
    paragraphs.append("I'm reaching out to chat about a back-linking opportunity between memberstack.com and " + re.findall(domain_regex, target_url, flags = re.I | re.M)[0] + ". Is that something you've done in the past or are excited to learn more about?")
    paragraphs.append("I get a fair few of these emails myself so totally understand if you hit archive 🤘")
    paragraphs.append("I'm particularly interested in a blog post you have on " + topic + ". In it you mention '" + anchor_text + "' - we have a detailed post on this, would you consider linking out to the Memberstack blog?")
    paragraphs.append("Here is the link for your convenience:")
    paragraphs.append(our_url)
    paragraphs.append("I'm wary of information overload so I won't yet go into the benefits those links can provide the both of us - but absolutely happy to chat about it more.")
    paragraphs.append("P.S. You're also probably wondering what Memberstack even is?")
    paragraphs.append("Memberstack helps Webflow developers build web apps. Think memberships, subscriptions, payments, and authentication. We're backed by YC, with over 50,000 users and the likes of Slack, Finsweet, Flowbase, and American airlines as some of our customers.")

    return "\n\n".join(paragraphs)

def duncan_email(recipient_name, target_url, topic, our_url, anchor_text, link_exchange):
    paragraphs = []
    paragraphs.append("Hey " + recipient_name + ", happy " + calendar.day_name[datetime.today().weekday()] + " 👋")
    paragraphs.append("Do you make updates to blog posts on " + re.findall(domain_regex, target_url, flags = re.I | re.M)[0] + " based on suggestions?")
    paragraphs.append("✅ If yes… I'm on the content team at memberstack.com (DR 73) and I'm trying to get our blog posts in front of more people. We have 2,000+ customers including American Airlines, Slack, and Entreprenuer.com and they used us to build web apps with Webflow.")
    paragraphs.append("❌ If not, you can archive this email 🤘")
    paragraphs.append("Would you be willing to mention Memberstack in your article on " + topic + "? If yes, I can suggest adding it where you mention '" + anchor_text + "'.")
    paragraphs.append("We have a detailed post on this, which you can find here:")
    paragraphs.append(our_url)
    if (link_exchange == "True"):
        paragraphs.append("And I'd like to return the favor in some way. If you share a few of your business goals I can brainstorm ways to make this worth the effort (social share, backlink, collab on a blog post, etc.).")
    else:
        paragraphs.append("And I'd like to return the favor in some way - just let me know if there is anything I can do for you.")
    paragraphs.append("Looking forward to your response!")
    paragraphs.append("Thank you,")
    paragraphs.append("Dimitris - Memberstack.com")

    return "\n\n".join(paragraphs)

#print(molly_email("Dimitris", "https://example.com/blog", "Custom Code in Webflow", "https://www.memberstack.com/blog/using-custom-code-in-webflow", "custom code", False))
#print(duncan_email("Dimitris", "https://example.com/blog", "Custom Code in Webflow", "https://www.memberstack.com/blog/using-custom-code-in-webflow", "custom code", False))