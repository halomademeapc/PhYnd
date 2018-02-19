% include('header.tpl', title="Play", subtitle="You are playing game " + gameid + " against PhYnd")

<p>test</p>

% include('board.tpl', interactive=True, gameid=gameid)

% #include ('footer.tpl')