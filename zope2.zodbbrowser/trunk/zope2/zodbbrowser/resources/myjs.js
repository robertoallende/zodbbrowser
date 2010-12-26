// getPath builds the path traversing the tree
var getPath = function(node) {
    if (node.data.title) { return ( getPath(node.parent) + "/" + node.data.title) ; }
    else { return "" }
};

  $(function(){
    $("#tree").dynatree({
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
      },
      onLazyRead: function(node){
              node.appendAjax({
                url: function() { return getPath(node) + "/tree"; }(),
                data: {key: node.data.key,
                       mode: "funnyMode"
                       }
              });
      }
    });
  });
