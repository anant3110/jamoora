c = Bus.control(s,1); //Play this

n = NetAddr("127.0.0.1", 8000); //Play this

( //Play for microphone audio
SynthDef(\busTest, {|bus|
    var in;
    in = Mix.new(AudioIn.ar([1,2]));
    Out.kr(bus, Pitch.kr(in, minFreq: 60, maxFreq: 1000, ampThreshold: 0.02, median: 7).cpsmidi.round(1));
}).add;
)
( //Play for microphone audio
r = Routine({
    inf.do({
        var val = c.getSynchronous;
        n.sendMsg(\pitch, val);
        0.01.wait;
    });
});
)
b = Synth(\busTest, [\bus, c]); //Play for microphone audio
r.play; // Play for microphone audio



( //Play for midi audio
SynthDef("umbSinewave",{
    arg freq=440, gate=1, amp=1, pan=0;
    var x;
    x = SinOsc.ar(freq, 0, amp);
    x = EnvGen.kr(Env.adsr(0.01,0.3,0.5,1,0.6,-4),gate,doneAction: 2) * x;
    Out.ar(0, Pan2.ar(x,pan));
}).add;
)


( //Play for midi audio
var keys;
keys = Array.newClear(128);

MIDIIn.connect;

~noteOnFunc = {arg src, chan, num, vel;
    var node;
    node = keys.at(num);
    if (node.notNil, {
        node.release;
        keys.put(num, nil);
    });
    node = Synth.tail(nil, "umbSinewave", [\freq, num.midicps, \amp, vel/127]);
    keys.put(num, node);
    n.sendMsg(\pitch, num);

};
MIDIIn.addFuncTo(\noteOn, ~noteOnFunc);

~noteOffFunc = {arg src, chan, num, vel;
    var node;
    node = keys.at(num);
    if (node.notNil, {
        node.release;
        keys.put(num, nil);
    });
};
MIDIIn.addFuncTo(\noteOff, ~noteOffFunc);
)
