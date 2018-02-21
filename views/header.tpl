<script
  src="http://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
<h1>phÿnd</h1>
<nav>
    <a href="/">Home</a>
    <a href="/play">Play</a>
    <a href="/stats">Stats</a>
    <a href="/about">About</a>
</nav>
% if title:
    <h2>{{title}}</h2>
% end
% if subtitle:
    <p>{{subtitle}}</p>
% end