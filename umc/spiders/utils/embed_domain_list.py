host_domain_list = \
    [
        "gomostream.com",
        "gcloud.live",
        "www.fembed.com",
        "vidtodo.com",
        "www.vidlox.me",
        "vidlox.tv",
        "gorillavid.in",
        "xstreamcdn.com",
        "vidnode.net",
        "vidcloud.icu",
        "vev.io",
        "vev.red",
        "truhd.xyz",
        "oyohd.com",
        "vidohd.com",
        "gounlimited.to",
        "hdv.fun",
        "uptostream.com",
        "vidcloud.co",
        "mediashore.org",
        "vidcloud.to",
        "videojsplus.com",
        "vidlocker.xyz",
        "ok.ru",
        "hqq.tv",
        "ghfkk.com",
        "vcdn.io",
        "mixdrop.co",
        "loadvid.online",
        "clipwatching.com",
        "putload.tv",
        "mp4upload.com",
        "afdah.info",
        "linkshrink.online",
        "vcstream.to",
        "oyohd.com",
        "oload.stream",
        "waaw.tv",
        "vidoza.net",
        "vidlox.me",
        "vidup.io",
        "vidup.icu",
        "vidia.tv",
        "prostream.to",
        "tunestream.net",
        "upfiles.pro",
        "player.clipot.tv",
        "vidlink.org",
        "viduplayer.com",
        "moviemaniac.org",
        "hindilinks4uto.com",
        "newsexit.org",
        "vidup.me",
        "www.dailymotion.com",
        "nxload.com",
        "video66.org",
        "playbb.me",
        "www.yourupload.com",
        "embed.daebakdrama.com",
        "videobin.co",
        "vidcloud9.com",
        "www.speedwatch.io",
        "p.walldrama.com",
        "scenelife.org",
        "www.vidbull.tv",
        "pkspeed.net",
        "mixdrop.to",
        "netu.best",
        "uqload.com",
        "www.fsimg.info",
        "embed.mystream.to",
        "upvid.host",
        "embed.mystream.to",
        "www.core1player.com"
    ]
# hosts link regex
host_embed_patterns = [
    r"//www.fembed.com/v/[a-zA-Z0-9]+\/?",
    r"//mixdrop.co/e/[a-zA-Z0-9]+\/?",
    r"//hqq.tv/player/embed_player.php\?vid=[a-zA-Z0-9&=]+",
    r"//vidlox.me/embed-[a-zA-Z0-9]+\.html",
    r"//www.vidlox.tv/embed-[a-zA-Z0-9-]+\.html",
    r"//vidsrc.me/embed/[a-zA-Z0-9]+\/?",
    r"//truhd.xyz/embed/[a-zA-Z0-9]+\/?",
    r"//oyohd.com/player/embed_player.php\?vid=[a-zA-Z0-9]+",
    r"//vidohd.com/v/[a-zA-Z0-9]+\-[a-zA-Z0-9]+\/?",
    r"//hxload.co/embed/[a-zA-Z0-9]+\/?",
    r"//gounlimited.to/embed-[a-zA-Z0-9]+\.html",
    r"//api.hdv.fun/embed/[a-zA-Z0-9]+",
    r"//uptostream.com/iframe/[a-zA-Z0-9]+",
    r"//vidcloud.co/embed/[a-zA-Z0-9]+",
    r"//mediashore.org/v/[a-zA-Z0-9]+",
    r"//vidcloud.to/public/dist/index.html\?id=[a-zA-Z0-9]+",
    r"//www.videojsplus.com/v/[a-zA-Z0-9]+",
    r"//vidlocker.xyz/embed-[a-zA-Z0-9]+\.html",
    r"//ok.ru/videoembed/[0-9a-zA-Z]+",
    r"//ghfkk.com/player/[0-9a-zA-Z]+/?",
    r"//vcdn.io/v/[0-9a-zA-Z]+",
    r"//clipwatching.com/embed-[a-zA-Z0-9]+\.html",
    r"//putload.tv/embed-[0-9a-zA-Z]+\.html",
    r"//gcloud.live/v/[0-9a-zA-Z]+",
    r"//gomostream.com/movie/[a-zA-Z0-9-]+",
    r"//www.mp4upload.com/embed-[0-9a-zA-Z]+\.html",
    r"//loadvid.online/embed/[a-zA-Z0-9]+",
    r"//afdah.info/embed[0-9]?/[0-9a-zA-Z]+",
    r"//linkshrink.online/v/[0-9A-Za-z-]+",
    r"//vcstream.to/embed/[0-9a-zA-Z./-]+",
    r"//oyohd.com/player/embed_player.php\?vid=[0-9a-zA-Z;=&]+",
    r"//oload.stream/embed/[0-9a-zA-Z_]+/?",
    r"//database.gdriveplayer.us/player\.php\?[0-9a-zA-Z&=]+",
    r"//waaw.tv/player/embed_player.php\?vid=[a-zA-Z0-9]+",
    r"///player/embed_player.php\?vid=[a-z0-9A-Z]+",
    r"//vidoza.net/embed-[0-9a-zA-Z]+\.html",
    r"//vidtodo.com/embed-[0-9a-zA-Z]+\.html",
    r"//vev.io/embed/[0-9a-zA-Zx&]+",
    r"//vev.red/embed/[a-zA-Z0-9]+",
    r"//vidup.io/embed/[0-9a-zA-Z]+",
    r"//vidia.tv/embed-[0-9a-zA-Z]+\.html",
    r"//prostream.to/embed-[0-9a-zA-Z]+\.html",
    r"//tunestream\.net/emb\.html\?[a-z0-9A-Z=./]+",
    r"//player.clipot.tv/player.php\?id=[0-9a-zA-Z&=://.]+",
    r"//upfiles.pro/embed-[0-9a-zA-Z]+\.html",
    r"//vidlink.org/embed/[0-9a-zA-Z]+",
    r"//viduplayer.com/embed-[0-9a-zA-Z]+\.html",
    r"//vidop.icu/embed/[a-zA-Z0-9&]+",
    r"//moviemaniac.org/v/[a-zA-Z0-9]+",
    r"//hindilinks4uto.com/player/embed_player.php\?vid=[a-zA-Z#=]+",
    r"//newsexit.org/embed-[a-zA-Z0-9]+\.html",
    r"//oload.space/embed/[a-zA-Z0-9_]+",
    r"//vidup.me/embed-[a-zA-Z0-9]+\.html",
    r"//vidnode.net/load\.php\?id=[^\"^\']*",
    r"//www.dailymotion.com/embed/video/[a-zA-Z0-9]+",
    r"//nxload.com/embed/[a-z0-9A-Z]+",
    r"//video66.org/new/[a-zA-Z0-9=&?_.-]+flv",
    r"//video66.org/embed.php\?w=[a-zA-Z0-9=&_/-]+\.mp4",
    r"//playbb.me/new/[a-zA-Z0-9&=]",
    r"//www.yourupload.com/embed/[a-zA-Z0-9]+",
    r"//videobin.co/embed-[a-zA-Z0-9]+\.html",
    r"//vidcloud9.com/load\.php\?id=[a-zA-Z0-9=&+-]+",
    r"//vidcloud9.com/server\.php\?id=[a-zA-Z0-9=&+-]+",
    r"//www.speedwatch.io/e/[a-zA-Z0-9]+\.html",
    r"//p.walldrama.com/player/[a-zA-Z0-9]+",
    r"//scenelife.org/player/embed_player\.php\?vid=[a-zA-Z0-9]+",
    r"//www.vidbull.tv/embed/[a-zA-Z0-9]+",
    r"//pkspeed.net/embed-[a-zA-Z0-9]+\.html",
    r"//cloudvideo.tv/embed-[a-zA-Z0-9]+",
    r"/cloudvideo.tv/emb\.html\?[a-z0-9A-Z=./_]+",
    r"//mixdrop.to/e/[a-zA-Z0-9]+",
    r"//netu.best/player/embed_player\.php\?vid=[a-zA-Z0-9=#]+",
    r"//uqload.com/embed-[a-z0-9A-Z]+\.html",
    r"//www.core1player.com/v/[a-zA-Z0-9]+",
    r"//embed.mystream.to/[a-zA-Z0-9]+",
    r"//upvid.host/embed-[a-zA-Z0-9]+\.html",
    r"//uptostream.com/iframe/[a-zA-Z0-9]+",
    r"//www.fsimg.info/v/[a-zA-Z0-9-]+",
    r"//upvid.co/embed-[a-zA-Z0-9]+\.html"
]


# def pattern_mapper(pattern):
#     p_w_http_ignore = "(?!" + pattern[0:6] + ")?" + pattern[6:]
#     return p_w_http_ignore
#
#
# host_embed_patterns = list(map(pattern_mapper, host_embed_patterns))

# not a detail page but has embedlinks
_not_detail_pages = [
    r"https://uwatchfreetv.xyz/\?trembed=[0-9]&trid=[0-9]+&trtype=[0-9]",
    r"https://www.bolly2tolly.net/\?trembed=[0-9]&trid=[0-9]+&trtype=[0-9]",
    r"https://waaw.tv/watch_video.php\?v=[0-9a-zA-Z]+",
    r"https://mixdrop.co/f/[a-zA-Z0-9]+",
    r"https://vidup.io/[a-zA-Z0-9]+",
    r"https://vidia.tv/[0-9a-zA-Z]+\.html",
    r"https://vidia.tv/[0-9a-zA-Z]+",
    r"https://vidoza.net/[0-9a-zA-Z]+(?:\.html)?",
    r"https://vidlox.me/[a-zA-Z0-9]+",
    r"https://prostream.to/[a-zA-Z0-9]+"
    r"https://cloudvideo.tv/[0-9a-zA-Z]+",
    r"https://vev.io/[a-zA-Z0-9]+",
    r"https://gounlimited.to/[0-9a-zA-Z]+",
    r"https://clipwatching.com/[0-9a-zA-Z]+",
    r"https://vidcloud.co/v/[a-z0-9A-Z]+",
    r"https?://nites.tv/\?trembed=[0-9]&trid=[0-9]+&trtype=[0-9]",
    r"https://vidnode.net/streaming\.php\?id=[^\"^\']*",
    r"https://www.losmovies.us/external/[a-zA-Z0-9=]+",
    r"https://prostream.to/[a-zA-Z0-9]+\.html",
    r"http://gounlimited.to/[a-z0-9A-Z]+",
    r"https://embed.daebakdrama.com/watch/[a-zA-Z0-9]+",
    r"https://videobin.co/[a-zA-Z0-9]+",
    r"https://vidcloud9.com/streaming\.php\?id=[a-zA-Z0-9+=&%-]+",
    r"https://www.uwatchfree.ms/[a-zA-Z0-9]+\.php\?vid=[a-zA-Z0-9]+",
]


# TODO: vidup.io and vev.io are not returning embed link

# notes::
# r"^https://www.vidbull.tv/embed/[0-9]+"  ---site==vmoviez.bz ,, gives porn in follow links
# r"https://mystream.to/watch/[a-zA-Z0-9]+",r"https://embed.mystream.to/[a-zA-Z0-9]+",==> even splash donot give embedlink
# r"https://onlystream.tv/e/[a-zA-Z0-9]+\/?" , r"https://onlystream.tv/[0-9a-zA-Z]+",==> cannot filter broken
# r"https://vshare.eu/embed-(.*)\.html", ==> ajax request
#  r"https://cloudvideo.tv/emb.html\?.*", ==> ajax request


# https://vidcloud9.com/streaming.php?id=NDA3MzU=&title=Power+-+Season+1+Episode+01%3A+Not+Exactly+How+We+Planned&typesub=SUB&sub=L3Bvd2VyLXNlYXNvbi0xLWVwaXNvZGUtMDEtbm90LWV4YWN0bHktaG93LXdlLXBsYW5uZWQvcG93ZXItc2Vhc29uLTEtZXBpc29kZS0wMS1ub3QtZXhhY3RseS1ob3ctd2UtcGxhbm5lZC52dHQ=&cover=L3Bvd2VyLXNlYXNvbi0xLWF3dy9jb3Zlci5wbmc=