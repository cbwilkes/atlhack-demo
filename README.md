# HackChat

HackChat is an example application showing basic usage of Google [AppEngine][1]
in [Python][2]. Users can write, save, and view simple text-based messages.

Messages are stored in AppEngine's datastore via the [`ndb`][3] library.
Possible extensions include using the [`user`][4] library to authenticate
users, using [jinja2][6] and [Bootstrap][7] to make it pretty, or anything else
you can think of.

[1]: https://developers.google.com/appengine
[2]: https://python.org
[3]: https://developers.google.com/appengine/docs/python/ndb/
[4]: https://developers.google.com/appengine/docs/python/users/
[5]: http://webapp-improved.appspot.com/
[6]: http://jinja.pocoo.org/docs/
[7]: http://twitter.github.com/bootstrap/
