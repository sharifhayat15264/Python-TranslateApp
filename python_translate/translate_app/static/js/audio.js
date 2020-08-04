// Handle audio record and upload
$(document).ready(function() {
    // webkitURL is deprecated but nevertheless
    URL = window.URL || window.webkitURL;

    var gumStream; 						// stream from getUserMedia()
    var recorder; 						// WebAudioRecorder object
    var input; 							// MediaStreamAudioSourceNode  we'll be recording
    var encodingType; 					// holds selected encoding for resulting audio (file)
    var encodeAfterRecord = true;       // when to encode
    var audio_blob;                     // blob

    // shim for AudioContext when it's not avb.
    var AudioContext = window.AudioContext || window.webkitAudioContext;
    var audioContext; // new audio context to help us record

    // add events to those 2 buttons
    recordButton.addEventListener("click", startRecording);
    stopButton.addEventListener("click", stopRecording);

    // A Stopwatch instance that displays its time nicely formatted.
    var stopwatch = new Stopwatch(function(runtime) {
       // format time as m:ss.d
       var minutes = Math.floor(runtime / 60000);
       var seconds = Math.floor(runtime % 60000 / 1000);
       var decimals = Math.floor(runtime % 1000 / 100);
       var displayText = "Time: " + minutes + ":" + (seconds < 10 ? "0" : "") + seconds + "." + decimals;

       // writing output to screen
       $("#time").html(displayText);
    });

    var previous = false;

    function startRecording() {
        /*
            Simple constraints object, for more advanced features see
            https://addpipe.com/blog/audio-constraints-getusermedia/
        */

        var constraints = { audio: true, video:false }

        /*
            We're using the standard promise based getUserMedia()
            https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
        */

        navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
            /*
                create an audio context after getUserMedia is called
                sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
                the sampleRate defaults to the one set in your OS for your playback device
            */
            audioContext = new AudioContext();

            // assign to gumStream for later use
            gumStream = stream;

            /* use the stream */
            input = audioContext.createMediaStreamSource(stream);

            // get the encoding
            encodingType = "wav";

            if (previous) {
                // resetting stopwatch
                stopwatch.resetLap();
                previous = false;
            }

            // starting
            stopwatch.startStop();

            recorder = new WebAudioRecorder(input, {
              workerDir: "/static/js/", // must end with slash
              encoding: encodingType,
              numChannels: 2, // 2 is the default, mp3 encoding supports only 2
              onEncoderLoading: function(recorder, encoding) {
                // show "loading encoder..." display
                //__log("Loading " + encoding + " encoder...");
              },
              onEncoderLoaded: function(recorder, encoding) {
                // hide "loading encoder..." display
                // __log(encoding + " encoder loaded");
              }
            });

            recorder.onComplete = function(recorder, blob) {
                gumStream.getAudioTracks()[0].stop();
                audio_blob = blob;
            }

            recorder.setOptions({
              timeLimit: 120,
              encodeAfterRecord: encodeAfterRecord,
              ogg: {quality: 0.5},
              mp3: {bitRate: 160}
            });

            // start the recording process
            recorder.startRecording();

        }).catch(function(err) {
            // enable the record button if getUSerMedia() fails
            $("#recordButton").attr("disabled", false);
            $("#stopButton").attr("disabled", true);
        });

        // disable the record button
        $("#recordButton").attr("disabled", true);
        $("#stopButton").attr("disabled", false);
    }

    function stopRecording() {
        // stop microphone access
        gumStream.getAudioTracks()[0].stop();

        previous = true;

        // stopping
        stopwatch.startStop();

        // disable the stop button
        $("#recordButton").attr("disabled", false);
        $("#stopButton").attr("disabled", true);

        $('#submit').prop('disabled', false);
        $('#submit').removeClass('disable-btn');

        // tell the recorder to finish the recording (stop recording + encode the recorded audio)
        recorder.finishRecording();
    }

    $('#submit').on('click', function() {
        var btn = $(this);
        btn.html('Translating...').prop('disabled', true).addClass('disable-btn');

        $("#stopButton").attr("disabled", true);

        var myFile = new Blob([audio_blob], { type: "audio/wav" });
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        var url = "translate_speech/";
        var data = new FormData();
        data.append('source', $('#source option:selected').val());
        data.append('destination', $('#destination option:selected').val());
        data.append('audio_file', myFile);
        data.append('csrfmiddlewaretoken', csrf);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function(data) {
                $("#output").val(data.translated);
                createDownloadLink(data.translated_file);

                $("#recordButton").attr("disabled", false);
                $("#submit").html("Translate");
            },
            error: function(request, status, error) {
                $("#recordButton").attr("disabled", false);
                $("#submit").html("Translate");
            },
            cache: false,
            contentType: false,
            processData: false
        });

        // resetting stopwatch
        stopwatch.resetLap();
    });

    function createDownloadLink(translated_file) {
        $("#recordingsList").empty();

        var au = document.createElement('audio');
        var li = document.createElement('li');
        var link = document.createElement('a');

        // add controls to the <audio> element
        au.controls = true;
        au.src = translated_file;

        // link the a element to the blob
        link.href = translated_file;
        link.download = new Date().toISOString() + '.' + 'wav';
        link.innerHTML = link.download;

        // add the new audio and a elements to the li element
        li.appendChild(au);
        li.appendChild(link);

        // add the li element to the ordered list
       document.getElementById("recordingsList").appendChild(li);
    }
});
