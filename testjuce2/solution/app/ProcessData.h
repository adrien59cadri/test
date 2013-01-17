#pragma once

//on gere une frame floatante, et n channels, la framerate
//on ne gere pas de format de groupe de channel dans des bus
//
//ccette struct n est pas synchronisee, et supposee acccedee uniquement dans le threaad audio

struct ProcessData{
	const float ** _inputbuffers;
	float ** _outputbuffers;
	int _nframes;
	int _nOutputBuffers;
	int _nInputBuffers;
	float _framerate;
};