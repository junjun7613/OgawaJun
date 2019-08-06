$(function(){
const viewer = new OpenSeadragon({
            id: "contentDiv",
            prefixUrl: "openseadragon-bin-2.4.0/images/",
    	    tileSources: {
        		type: 'image',
        		url:  './pictures/$ILN-05-03_00722.jpg',
        		buildPyramid: false
    			}
        });
	$(".overlay").hover(
	function(){
        /*viewer.addHandler("open", function(event) {*/
            var elt = document.createElement("div");
            elt.className = "runtime-overlay";
            elt.style.background = "green";
            elt.style.opacity = "0.4";
            viewer.addOverlay({
                element: elt,
                location: new OpenSeadragon.Rect(0.05, 0.03, 0.350, 0.079),
                rotationMode: OpenSeadragon.OverlayRotationMode.BUILDING_BOX
            });

            /*elt = document.createElement("div");
            elt.className = "runtime-overlay";
            elt.style.background = "red";
            elt.style.opacity = "0.5";
            elt.style.height = "100px";
	    elt.style.opacity = "0.4";
            viewer.addOverlay({
                element: elt,
                location: new OpenSeadragon.Rect(0.71, 0.21, 0.069, 0.069),
                width: 0.5
            });
            elt = document.createElement("div");
            elt.className = "runtime-overlay";
            elt.style.background = "white";
            elt.style.opacity = "0.5";
            elt.style.outline = "5px solid pink";
            elt.style.width = "100px";
            elt.style.height = "100px";
            elt.textContent = "Not scaled, centered in the middle";
            viewer.addOverlay({
                element: elt,
                location: new OpenSeadragon.Point(0.5, 0.5),
                placement: OpenSeadragon.Placement.CENTER,
                checkResize: false,
                rotationMode: OpenSeadragon.OverlayRotationMode.EXACT
            });*/
        /*});*/
},
function(){
viewer.clearOverlays();
}
);
        $("#hideOverlays").click(function(){
            $(".runtime-overlay").toggle();
        });
        $("#rotate").click(function() {
            viewer.viewport.setRotation(viewer.viewport.getRotation() + 22.5);
            $("#degrees").text(viewer.viewport.getRotation() + "deg");
        });
});