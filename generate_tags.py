import os
import glob

TAG_DIR = 'tag'
POSTS_DIR = '_posts'

def get_tags_from_posts():
    tags = set()
    for post_file in glob.glob(os.path.join(POSTS_DIR, '*.md')):
        print(f"Reading file: {post_file}")
        with open(post_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('tags:') or line.startswith('tag:'):
                    tags_line = line.strip().replace('tags:', '').replace('tag:', '').strip()
                    print(f"Found tags line: {tags_line}")
                    post_tags = [tag.strip() for tag in tags_line.strip('[]').split(',')]
                    tags.update(post_tags)
                    break
    print(f"Tags found: {tags}")
    return tags

def create_tag_pages(tags):
    if not os.path.exists(TAG_DIR):
        os.makedirs(TAG_DIR)
    for tag in tags:
        tag_filename = f"{tag}.md"
        tag_filepath = os.path.join(TAG_DIR, tag_filename)
        if not os.path.exists(tag_filepath):
            with open(tag_filepath, 'w', encoding='utf-8') as file:
                file.write(f"---\nlayout: tagpage\ntitle: \"Tag: {tag}\"\ntag: {tag}\n---\n")
            print(f"Generated tag page for {tag}")

if __name__ == "__main__":
    tags = get_tags_from_posts()
    create_tag_pages(tags)
