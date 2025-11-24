from pathlib import Path
from ampel.cli.JobCommand import JobCommand

JOB_FILE = "/Users/emorymurff/Dropbox/leiden/qpes/timewise_config_ampel_job.yml"
CONFIG_FILE = "/Users/emorymurff/Dropbox/leiden/qpes/qpes/ampel_config.yml"

cmd = JobCommand()
parser = cmd.get_parser()
args = vars(
    parser.parse_args(
        [
            "--schema",
            str(JOB_FILE),
            "--config",
            str(CONFIG_FILE),
            
        ]
    )
)
cmd.run(args, unknown_args=())
