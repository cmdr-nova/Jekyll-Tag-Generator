# Jekyll-Tag-Generator
Do you run a Jekyll blog? Do you use tags to add hashtags to your posts, which, in-turn, creates a sort of archive for your sit? Are you tired of having to make those tag pages manually, with your fingers and a keybaord, like a *caveman*?

Well, buddy, do I have the solution for you!

In your setup, in order for this to work, you should be using a tagpage.html in your _layouts directory that looks something like this:
```
---
layout: default
---
<div id="main">
  <table>
    <tr>
    <td>


<a class="read-title" href="/">Tag: {{ page.tag }}</a>
<br />
<ul>
{% for post in site.tags[page.tag] %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date |     date_to_string }})<br>
    {{ post.description }}
  </li>
{% endfor %}
</ul>
</div>


{% include archive.html %}

  </td>
  </tr>
  </table>

</div>
```
Obviously, you'll want to change this to reflect your CSS elements properly, and rename things if you like.

You should also have a collecttags.html in your _includes directory, that looks like this:
```
{% assign rawtags = "" %}
{% for post in site.posts %}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% assign site.tags = "" %}
{% for tag in rawtags %}
  {% if tag != "" %}
    {% if tags == "" %}
      {% assign tags = tag | split:'|' %}
    {% endif %}
    {% unless tags contains tag %}
      {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
    {% endunless %}
  {% endif %}
{% endfor %}
```
In head.html in the _includes directory, add this:
```
{% if site.tags != "" %}
    {% include collecttags.html %}
  {% endif %}
```
Finally, create an archive.html where all of your tags can be viewed like an archive for visitors to read, and put it in your _includes directory:
```
<p class="cloud">
{% capture temptags %}
  {% for tag in site.tags %}
    {{ tag[1].size | plus: 1000 }}#{{ tag[0] }}#{{ tag[1].size }}
  {% endfor %}
{% endcapture %}
{% assign sortedtemptags = temptags | split:' ' | sort | reverse %}
{% for temptag in sortedtemptags %}
  {% assign tagitems = temptag | split: '#' %}
  {% capture tagname %}{{ tagitems[1] }}{% endcapture %}
  <a href="/tag/{{ tagname }}"><code class="highligher"><nobr>{{ tagname    }}</nobr></code></a>
{% endfor %}
</p>
```
Now, take both scripts in this repository and put them in your jekyll blog's root directory, and in terminal run:
```
./serve.sh
```
(of course, only run this while you're building locally, and/or writing new posts, so that the python script creates new tag pages based on tags you're using in your posts)

In order for the script to grab tags, a post's front matter should include:
```
tag: [example_tag, tag2]
```
And, of course! Add both generate_tags.py and serve.sh to your .gitignore file, because you have no reason to upload these to your website, or Github Pages. And that's it! Voila!
