# Use the built-in blog

The blog is meant for presenting stories about your family history research.

In the Gramps database, blog posts are represented as sources with a note attached, containg the blog's text, and optionally, media files for the images of the blog post. Gramps Web treats every source with a tag `Blog` as blog article.

## Add a blog post

To add a blog post, you can use Gramps Web or Gramps Dekstop ([synchronized](sync.md) with Gramps Web), the steps are the same in both cases:

- Add a new source. The title of the source will be the title of your blog post, the author of the source will be the author of the post.
- Optionally, associate the source with a repository corresponding to your Gramps Web blog
- Add a new note to the source. Write your blog post and copy the text into the note.
- Optionally, add one or more media files to your source. The first media file will be taken as the post preview picture shown above the text. All media files will be shown below the text as a gallery.
- Add the label `Blog` to the source (create it if it doesn't exist)

## Relation between blog and sources

Since blog posts are just sources, all blog articles also appear on the list of sources and show up as sources in searches. In the source view, there is a button "show in blog" that will take you to the blog view for that blog post. The URL of the blog post also contains the Gramps ID of the corresponding source, so an article at `yourdomain.com/blog/S0123` corresponds to the source at `yourdomain.com/source/S0123`.

At the bottom of every blog post, there is a button "details" that will take you to the source view.