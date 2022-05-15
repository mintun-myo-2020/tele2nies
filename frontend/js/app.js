document.addEventListener("DOMContentLoaded", () => {
    var btn = document.getElementById("btn");
    var video = document.getElementById("vid");
    var mediaDevices = navigator.mediaDevices;
    vid.muted = true;
    btn.addEventListener("click", () => {
        console.log('webcam opened')
      // Accessing the user camera and video.
      mediaDevices
        .getUserMedia({
          video: true,
          audio: true,
        })
        .then((stream) => {

          // Changing the source of video to current stream.
          video.srcObject = stream;
          video.addEventListener("loadedmetadata", () => {
            video.play();
          });
        })
        .catch(alert);
    });
  });

document.getElementById('close_btn').addEventListener('click', cameraoff)

function cameraoff() {
    let videoElem = document.getElementById("vid")
    const stream = videoElem.srcObject;
    if (stream) {
      const tracks = stream.getTracks();

      tracks.forEach(function (track) {
        track.stop();
      });

      videoElem.srcObject = null;
      console.log('webcam closed')
   }
}