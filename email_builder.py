import re

def molly_email(recipient_name, target_url, topic, our_url, anchor_text):
    domain_regex = "^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)"

    paragraphs = []
    paragraphs.append("Hey " + recipient_name + ",")
    paragraphs.append("Dimitris here from the content team at memberstack.com (DR 72).")
    paragraphs.append("I'm reaching out to chat about a back-linking opportunity between memberstack.com and " + re.findall(domain_regex, target_url, flags = re.I | re.M)[0] + ". Is that something you've done in the past or are excited to learn more about?")
    paragraphs.append("I get a fair few of these emails myself so totally understand if you hit archive. You won't get any follow-up emails from me 🤘")
    paragraphs.append("I'm particularly interested in a blog post you have on " + topic + ". In it you mention '" + anchor_text + "' - we have a detailed post on exactly this, would you consider linking out to the Memberstack blog?")
    paragraphs.append("Here is the link for your convenience:")
    paragraphs.append(our_url)
    paragraphs.append("I'm wary of information overload so I won't yet go into the benefits those links can provide the both of us - but absolutely happy to chat about it more.")
    paragraphs.append("P.S. You're also probably wondering what Memberstack even is?")
    paragraphs.append("Memberstack helps Webflow developers build web apps. Think memberships, subscriptions, payments, and authentication. We're backed by YC, with over 50,000 users and the likes of Slack, Finsweet, Flowbase, and American airlines as some of our customers.")

    return "\n\n".join(paragraphs)

def duncan_email():
    pass
