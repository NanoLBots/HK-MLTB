from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f"start{CMD_SUFFIX}"
        self.MirrorCommand = [f"mirror11{CMD_SUFFIX}", f"m11{CMD_SUFFIX}"]
        self.QbMirrorCommand = [f"qbmirror11{CMD_SUFFIX}", f"qm11{CMD_SUFFIX}"]
        self.JdMirrorCommand = [f"jdmirror11{CMD_SUFFIX}", f"jm11{CMD_SUFFIX}"]
        self.YtdlCommand = [f"ytdl11{CMD_SUFFIX}", f"y11{CMD_SUFFIX}"]
        self.LeechCommand = [f"leech11{CMD_SUFFIX}", f"l11{CMD_SUFFIX}"]
        self.QbLeechCommand = [f"qbleech11{CMD_SUFFIX}", f"ql11{CMD_SUFFIX}"]
        self.JdLeechCommand = [f"jdLeech{11CMD_SUFFIX}", f"jl11{CMD_SUFFIX}"]
        self.YtdlLeechCommand = [f"ytdlleech11{CMD_SUFFIX}", f"yl11{CMD_SUFFIX}"]
        self.CloneCommand = f"clone{CMD_SUFFIX}"
        self.CountCommand = f"count{CMD_SUFFIX}"
        self.DeleteCommand = f"del{CMD_SUFFIX}"
        self.CancelTaskCommand = [f"cancel11{CMD_SUFFIX}", f"c{CMD_SUFFIX}"]
        self.CancelAllCommand = f"cancelall{CMD_SUFFIX}"
        self.ForceStartCommand = [f"forcestart11{CMD_SUFFIX}", f"fs11{CMD_SUFFIX}"]
        self.ListCommand = f"list{CMD_SUFFIX}"
        self.SearchCommand = f"search{CMD_SUFFIX}"
        self.StatusCommand = f"status11{CMD_SUFFIX}"
        self.UsersCommand = f"users11{CMD_SUFFIX}"
        self.AuthorizeCommand = f"authorize11{CMD_SUFFIX}"
        self.UnAuthorizeCommand = f"unauthorize11{CMD_SUFFIX}"
        self.AddSudoCommand = f"addsudo{CMD_SUFFIX}"
        self.RmSudoCommand = f"rmsudo{CMD_SUFFIX}"
        self.PingCommand = f"ping11{CMD_SUFFIX}"
        self.RestartCommand = f"restart11{CMD_SUFFIX}"
        self.StatsCommand = f"stats11{CMD_SUFFIX}"
        self.HelpCommand = f"help11{CMD_SUFFIX}"
        self.LogCommand = f"log11{CMD_SUFFIX}"
        self.ShellCommand = f"shell{CMD_SUFFIX}"
        self.AExecCommand = f"aexec{CMD_SUFFIX}"
        self.ExecCommand = f"exec{CMD_SUFFIX}"
        self.ClearLocalsCommand = f"clearlocals{CMD_SUFFIX}"
        self.BotSetCommand = [f"bsetting11{CMD_SUFFIX}", f"bs11{CMD_SUFFIX}"]
        self.UserSetCommand = [f"usetting11{CMD_SUFFIX}", f"us11{CMD_SUFFIX}"]
        self.BtSelectCommand = f"btsel11{CMD_SUFFIX}"
        self.RssCommand = f"rss11{CMD_SUFFIX}"


BotCommands = _BotCommands()
