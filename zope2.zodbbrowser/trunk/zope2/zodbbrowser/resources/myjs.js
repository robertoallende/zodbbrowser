// right panel 
var emptyRight = function(){
    $("#right").text("");
    };

var right = function(kind){
    $("#right").dynatree({
          initAjax: {
              url: kind,
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        // console.log('Right: ' + kind);
      },
      onDeactivate: function(node) {
        // console.log("-");
      }
    });
  };

// midle panel 
var emptyMiddle = function(){
    $("#middle").text("");
    };

var middle = function(){
    $("#middle").dynatree({
          initAjax: {
              url: "/list_kind",
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        switch (node.data.title) {
            case "Properties" : right('properties') ;  break;
            case "Callables" : right('callables') ; break;
            case "Properties and Callables" : right('properties_and_callables') ; break;
            case "Interfaces Provided" : right('properties') ; break;
            case "Adapts" : right('properties') ; break;
        }
        // XXX this makes a request twice 
        var rightTree = $("#right").dynatree("getTree");
        rightTree.reload();
      },
      onPostInit: function(isReloading, isError) {
         this.reactivate();
      },
      onDeactivate: function(node) {
        emptyRight();
      }
    });
  };


// Just for the left: getPath builds the path traversing the tree
var getPath = function(node) {
    if (node.data.title) { return ( getPath(node.parent) + "/" + node.data.title) ; }
    else { return "" ; }
};

// left panel
  $(function(){
    $("#left").dynatree({
          initAjax: {
              url: "/tree",
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        middle();
        var rightTree = $("#middle").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        $("#right").text("");
        $("#middle").text("");
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


