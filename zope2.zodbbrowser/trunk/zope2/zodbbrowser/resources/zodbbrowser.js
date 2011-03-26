// bottom panel 
var emptyBottom = function(){
    $("#bottom").text("");
    $("#status").text("");
    };

var bottom = function(nodepath, panelpath, nodename, kindof) {
    $.ajax({
          url: nodepath + kindof + nodename,
          dataType: "json",
          success: function(data) {
            $('#bottom').html(data['bottom']);
            $('#status').html("# " + data['status']);

           }
     });
};

// right panel 
var emptyRight = function(){
    $("#right").text("");
};

var right = function(nodepath, kind){
    $("#right").dynatree({
      initAjax: {
          url: nodepath + kind,
          data: { mode: "all" },
          dataType: "json"
          },
      onActivate: function(node) {
        elem = node.data.title;
        switch (kind) {
            case "/class_ancestors" : bottom(nodepath, getPath(node), node.data.title, "/class_source?"); 
                break;
            case "/properties-please" : bottom(nodepath, getPath(node), node.data.title, "/property_source?"); 
                break;
            case "/callables-please" : bottom(nodepath, getPath(node), node.data.title, "/method_source?");         
                break;
            case "/interfaces-please" : bottom(nodepath, getPath(node), node.data.title, "/interface_source?"); 
                break;
            case "/annotations" : bottom(nodepath, getPath(node), node.data.title, "/annotation_value?"); 
                break;
        }
      }
    });
  };

// middle panel 
var emptyMiddle = function(){
    $("#middle").text("");
    };

var middle = function(path){
    $("#middle").dynatree({
              children: [
                        {
                            "title": "Class and Ancestors"
                        }, 
                        {
                            "title": "Properties"
                        }, 
                        {
                            "title": "Callables"
                        }, 
                        {
                            "title": "Interfaces Provided"
                        },
                        {
                            "title": "Annotations"
                        }
                    ] ,
      onActivate: function(node) {
        switch (node.data.title) {
            case "Properties" : right(path, '/properties-please') ;  break;
            case "Callables" : right(path, '/callables-please') ; break;
            case "Interfaces Provided" : right(path, '/interfaces-please') ; break;
            case "Adapts" : right(path, '/adapts') ; break;
            case "Class and Ancestors" : right(path, '/class_ancestors') ; break;
            case "Annotations" : right(path, '/annotations') ; break;
        }
        // XXX this forces a request twice sometimes
        var rightTree = $("#right").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        emptyRight();
        emptyBottom();
      }
    });
  };


// Just for the left: getPath builds the path traversing the tree
var buildTree = function(node) {
    if (node.data.title) { return ( buildTree(node.parent) + "/" + node.data.title) ; }
    else { return "" ; }
};

var getPath = function(node) {
    var mypath = buildTree(node);
    return mypath.slice(12);
};


function getSmartFilterSetting(){
    if (window.location.href.indexOf('smart_filter=disabled') > 0){
        return 'disabled';
    }
    return '';
}

// left panel
  $(function(){
    $("#left").dynatree({
      initAjax: {
          url: "/tree",
          data: { mode: "all" , smart_filter:getSmartFilterSetting()},
      },
      ajaxDefaults: {
        cache: false, // for debug: Append random '_' argument to the request url to prevent caching.
        dataType: "json"
      },
      onActivate: function(node) {
        var mypath = getPath(node);
        middle(mypath);
        // XXX this forces a request twice sometimes
        var rightTree = $("#middle").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        emptyRight();
        emptyMiddle();
        emptyBottom();
      },
      onLazyRead: function(node){
                node.appendAjax({
                url: function() { return getPath(node) + "/tree"; }(),
                data: {key: node.data.key,
                       mode: "all",
                       smart_filter:getSmartFilterSetting()
                       }
              });
      }
    });
  });

// Panels using jQuery UI.Layout 

var myLayout; // a var is required because this page utilizes: myLayout.allowOverflow() method

$(document).ready(function () {	
	myLayout = $('body').layout({
        applyDefaultStyles: true,
    });

    myLayout.sizePane('east', 350);
    myLayout.sizePane('west', 500);
});



