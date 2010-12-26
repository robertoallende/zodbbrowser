  $(function(){
    $("#tree").dynatree({
      // In real life we would call a URL on the server like this:
          initAjax: {
              url: "/tree",
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        $("#echoActive").text(node.data.title);
      },
      onDeactivate: function(node) {
        $("#echoActive").text("-");
      }
    });
  });
