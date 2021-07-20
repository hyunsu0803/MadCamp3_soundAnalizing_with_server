# Flask Server && Sound Source Analyzer (madmom)

### 프로젝트 한 줄 소개
> 서버에 들어온 post 요청을 받아서 음원을 분석한 결과를 반환하는 프로그램 및 서버

### 팀원 소개
> hyunsu0803, PLJE

----------

### 프로젝트 상세 설명
+ server.py
>
> localhost:5000/react_to_flask 에서 POST 요청만을 처리한다.
>
> flask의 request로부터 file을 받아서 프로젝트 내의 data directory에 저장하고
> 
> 해당 파일을 main.audio_to_MIDI_notes()에 넘겨준다.
>
> main.audio_to_MIDI_notes로부터 반환된 음원 분석 결과를 parsing 하여 json 형식으로 클라이언트에게 반환한다.
>
> 반환되는 정보에는 각 음이 attack된 timing ('second')과 MIDI note code ('code')가 각각 json 객체의 key-value pair로 들어가있다.

+ main.py
> 
> server로부터 파일을 경로로 넘겨받는다.
> 
> madmom library의 features package 속 CNNPianoNoteProcessor와 ADSRNoteTrackProcessor를 이용해 음원으로부터 MIDI note를 추출해낸다.
>
> 분석 결과는 2-dimensional numpy array로 반환한다. 3개의 column과 음 개수만큼의 row로 이루어져 있으며 첫번째 column은 각 음의 attack timing, 두번쨰 column은 MIDI note이다. 
> 
> 음원 분석의 정확도를 높이기 위해 onset_threshold를 0.9로 높여주었다.
>
> piano 소리를 분석하기 위해 pitch_offset을 21로 설정해주었다. 따라서 이 프로그램으로는 피아노 소리만을 MIDI note로 올바르게 변환할 수 있다.


### main.py 프로젝트를 실행하려면 (음원 분석)
+ madmom 라이브러리를 설치하기 위해서 [madmom 공식 깃 레포지토리](https://github.com/CPJKU/madmom)를 원하는 폴더에 recursive clone 한다. 
  - pip install madmom으로는 최신 버전의 madmom을 다운받을 수 없는 경우도 있으니 (필자의 경우가 그러했다.) 안전하게 깃을 통해 다운받자.
  - [madmom documentation : install-from-source](https://madmom.readthedocs.io/en/latest/installation.html#install-from-source) 을 따라하면 된다. 
