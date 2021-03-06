% include('header.tpl', title="About")
<nav class="breadcrumb">
    <a class="breadcrumb-item" href="/">phÿnd</a>
    <span class="breadcrumb-item active">about</span>
</nav>

<h1 class="text-center">About phÿnd</h1>
<p class="lead text-center pt-3">Rudimentary machine learning tic-tac-toe</p>
<hr class="my-5">
<h2>How it works</h2>
<p class="lead">If you're wondering, "phÿnd" is supposed to be pronounced like "fiend".</p>
<p>phÿnd is a machine-learning (in the loosest sense of the term) application that plays tic-tac-toe. phÿnd knows nothing about
    the game in terms of strategy; it only knows which moves it has made and whether that move led to a loss. phÿnd initially
    chooses a spot to place its cross at random, leading to some embarassing losses. However, as phÿnd loses, it becomes
    progressively less likely to make those same decisions that led to a loss. It's a very inefficient system as a whole
    and the implementation could have been improved by accounting for matching translated scenarios, but I think it's still
    a good bit of fun in the end. </p>

<h2 class="mt-5">Inspiration</h2>
<div class="float-md-right col-lg-6 col-md-6 col-sm-12">
    <div class="embed-responsive embed-responsive-16by9">
        <iframe src="https://www.youtube.com/embed/R9c-_neaxeU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
</div>
<p class="lead">Menace is a real fiend.</p>
<p>phÿnd is based off of concepts in Menace, the machine-educable naughts-and-crosses engine. The two have a similar premise
    but menace is physically built on bead in matchboxes. Standupmaths has an excellent video on the project that you can
    see here. </p>
<div class="clearfix"></div>

<h2 class="mt-5">Technologies Used</h2>
<div class="card mb-4">
    <div class="card-body">
        <div class="float-sm-left">
            <h4>Material Design Spinner</h4>
            <p class="lead m-0">By Fran Pérez</p>
        </div>
        <div class="text-right">
            <a href="https://codepen.io/mrrocks/pen/EiplA" class="btn btn-primary">View Source</a>
        </div>
    </div>
</div>

<div class="card mb-4">
    <div class="card-body">
        <div class="float-sm-left">
            <h4>Material Design Bootstrap</h4>
            <p class="lead m-0">By MDBootstrap.com</p>
        </div>
        <div class="text-right">
            <a href="https://mdbootstrap.com" class="btn btn-primary">View Site</a>
        </div>
    </div>
</div>

<div class="card mb-4">
    <div class="card-body">
        <div class="float-sm-left">
            <h4>Bottle</h4>
            <p class="lead m-0">By Marcel Hellkamp </p>
        </div>
        <div class="text-right">
            <a href="https://bottlepy.org" class="btn btn-primary">View Site</a>
        </div>
    </div>
</div>
% #include ('footer.tpl')