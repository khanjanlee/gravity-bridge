//! `version` subcommand

#![allow(clippy::never_loop)]

use super::GorcCmd;
use abscissa_core::{Command, Options, Runnable};

/// `version` subcommand
#[derive(Command, Debug, Default, Options)]
pub struct VersionCmd {}

impl Runnable for VersionCmd {
    /// Print version message
    fn run(&self) {
        println!(
            "{} {}",
            GorcCmd::name(),
            GorcCmd::version()
        );
    }
}
