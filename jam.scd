c = Bus.control(s,1);

n = NetAddr("127.0.0.1", 8000);

(
SynthDef(\busTest, {|bus|
	var in;
	in = Mix.new(AudioIn.ar([1,2]));
	Out.kr(bus, Pitch.kr(in, minFreq: 60, maxFreq: 1000, ampThreshold: 0.02, median: 7).cpsmidi.round(1));
}).add;
)

(
r = Routine({
	inf.do({
		var val = c.getSynchronous;
		n.sendMsg(\pitch, val);
		0.01.wait;
	});
});
)

b = Synth(\busTest, [\bus, c]);

r.play;