# 2. BIPOLAR TRANSISTORS

The transistor is our most important example of an “active” component, a device that can amplify, producing an output
signal with more power in it than the input signal.

Devices with power gain are distinguishable by their ability to make oscillators, by feeding some output signal back
into the input.

The transistor is the essential ingredient of every electronic circuit, from the simplest ampliﬁer or oscillator to
the most elaborate digital computer. Integrated circuits (ICs), which have largely replaced circuits constructed
from discrete transistors, are themselves merely arrays of transistors and other components built from a single chip
of semiconductor material.

BJTs excel in accuracy and low noise, whereas FETs excel in low power, high impedance,
and high-current switching.

## First transistor model: current ampliﬁer

A bipolar transistor is a three-terminal device, in which a small current applied to the base
controls a much larger current ﬂowing between the collector and emitter.

## Some basic transistor circuits

**Transistor switch:** a small control current enables a much larger current to ﬂow in another circuit, is called
a transistor switch.

**Pulse generator:** By including a simple RC, you can make a circuit that gives a pulse output from a step input;
the time constant τ = RC determines the pulse width.

**Emitter follower:** It is called that because the output terminal is the emitter, which
follows the input (the base), less one diode drop:

**Emitter followers as voltage regulators:** The simplest regulated supply of voltage is simply a zener

**Emitter follower biasing:** When an emitter follower is driven from a preceding stage
in a circuit, it is usually OK to connect its base directly to the previous stage’s output.

**Current source:** Current sources, although often neglected, are as important and as useful as voltage sources.
They often provide an excellent way to bias transistors, and they are unequaled as “active loads” for super-gain
ampliﬁer stages and as emitter sources for differential ampliﬁers. Integrators, sawtooth generators, and ramp
generators need current sources.

**Unity-gain phase splitter:** Sometimes it is useful to generate a signal and its inverse, i.e., two signals 180°
out of phase. That’s easy to do – just use an emitter-degenerated ampliﬁer with a gain of −1.

**Transconductance:** the measure of how efficiently a transistor converts a small input voltage change into a
larger output current change. The voltage gain was then simply the ratio of collector (output) voltage swing to base
(input) voltage swing.

Before jumping into the complexity just ahead, let’s remind ourselves of the four transistor circuits we’ve seen, namely
the switch, emitter follower, current source, and common emitter ampliﬁer.

## Ebers–Moll model
