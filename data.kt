private const val CONFERENCE_DAY1_START = "2019-05-07T07:00:00-07:00"
private const val CONFERENCE_DAY1_END = "2019-05-07T22:00:01-07:00"
val TestConferenceDays = listOf(
	ConferenceDay(
		ZonedDateTime.parse(CONFERENCE_DAY1_START)),
	ConferenceDay(
		ZonedDateTime.parse(CONFERENCE_DAY2_START),
		ZonedDateTime.parse(CONFERENCE_DAY2_END)),
	ConferenceDay(
		ZonedDateTime.parse(CONFERENCE_DAY3_START),
		ZonedDateTime.parse(CONFERENCE_DAY3_END)))
val androidTag = Tag("1", Tag.CATEGORY_TOPIC, "track_android", 0, "Android", 0xFFAED581.toInt())
val tagsList = listOf(
	androidTag, cloudTag, webTag, sessionsTag, codelabsTag, beginnerTag,
	intermediateTag, advancedTag, themeTag)
val speaker1 = Speaker(
	id = "1")
val speaker3 = Speaker(
	id = "3",
	name = "Hans Moleman",
	imageUrl = "",
	company = "",
	biography = "")
val room = Room(id = "1", name = "Tent 1")
val session0 = Session(
	id = "0", title = "Session 0", description = "This session is awesome",
	startTime = TestConferenceDays[0].start, endTime = TestConferenceDays[0].end,
	isLivestream = false,
	room = room, sessionUrl = "", youTubeUrl = "", photoUrl = "", doryLink = "",
	tags = listOf(androidTag, webTag, sessionsTag),
	displayTags = listOf(androidTag, webTag),
	speakers = setOf(speaker1), relatedSessions = emptySet())
val sessionsList = listOf(session0, session1, session2, session3, sessionWithYoutubeUrl)
val sessionIDs = sessionsList.map { it.id }.toList()
val block1 = Block(
	title = "Keynote",
	type = "keynote",
	color = 0xffff00ff.toInt(),
	startTime = TestConferenceDays[0].start,
	endTime = TestConferenceDays[0].start.plusHours(1L))
val block2 = Block(
	title = "Breakfast",
	type = "meal",
	color = 0xffff00ff.toInt(),
	startTime = TestConferenceDays[0].start.plusHours(1L),
	endTime = TestConferenceDays[0].start.plusHours(2L))
val agenda = listOf(block1, block2)
private val userEvent0 = UserEvent()