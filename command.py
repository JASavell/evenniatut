"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import Command as BaseCommand
from evennia import default_cmds

import evennia

class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super(MuxCommand, self).has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None


class CmdMakeGM(default_cmds.MuxCommand): 
    """
    Change an account's GM status

    Usage:
      @gm <account>
      @ungm <account>

    """
    # note using the key without @ means both @gm !gm etc will work
    key = "gm"
    aliases = "ungm"
    locks = "cmd:perm(Developers)"
    help_category = "RP"

    def func(self):
        "Implement the command"
        caller = self.caller

        if not self.args:
            caller.msg("Usage: @gm account or @ungm account")
            return

        accountlist = evennia.search_account(self.args) # returns a list
        if not accountlist:
            caller.msg("Could not find account '%s'" % self.args)
            return
        elif len(accountlist) > 1:
            caller.msg("Multiple matches for '%s': %s" % (self.args, accountlist))
            return
        else:
            account = accountlist[0] 

        if self.cmdstring == "gm":
            # turn someone into a GM
            if account.permissions.get("Admins"):
                caller.msg("Account %s is already a GM." % account)
            else:
                account.permissions.add("Admins")
                caller.msg("Account %s is now a GM." % account)
                account.msg("You are now a GM (changed by %s)." % caller)
                account.character.db.is_gm = True
        else:
            # @ungm was entered - revoke GM status from someone
            if not account.permissions.get("Admins"):
                caller.msg("Account %s is not a GM." % account)             
            else:
                account.permissions.remove("Admins")
                caller.msg("Account %s is no longer a GM." % account)
                account.msg("You are no longer a GM (changed by %s)." % caller)
                del account.character.db.is_gm


ALLOWED_ATTRS = ("str", "con", "dex", "int", "wis", "cha")
ALLOWED_FIELDNAMES = ALLOWED_ATTRS + \
                     ("name", "advantages", "disadvantages")

def _validate_fieldname(caller, fieldname):
    "Helper function to validate field names."
    if fieldname not in ALLOWED_FIELDNAMES:
        err = "Allowed field names: %s" % (", ".join(ALLOWED_FIELDNAMES))
        caller.msg(err)
        return False
    if fieldname in ALLOWED_ATTRS and not value.isdigit():
        caller.msg("%s must receive a number." % fieldname)
        return False
    return True   

class CmdSheet(MuxCommand):
    """
    Edit a field on the character sheet
    
    Usage:
      @sheet field value
   
    Examples:
      @sheet name Ulrik the Warrior
      @sheet dex 12
      @sheet advantages Super strength, Night vision

    If given without arguments, will view the current character sheet.

    Allowed field names are:
       name,
       str, con, dex, int, wis, cha,
       advantages, disadvantages

    """

    key = "sheet"
    aliases = "editsheet"
    locks = "cmd: perm(Players)"
    help_category = "RP"

    def func(self):
        caller = self.caller
        if not self.args or len(self.args) < 2:
            # not enough arguments. Display the sheet
            if sheet:
                caller.msg(unicode(caller.db.charsheet))
            else:
                caller.msg("You have no character sheet.")
            return

        # if caller.db.sheet_locked:
            caller.msg("Your character sheet is locked.")
            return 

        # split input by whitespace, once
        fieldname, value = self.args.split(None, 1)
        fieldname = fieldname.lower() # ignore case

        if not _validate_fieldnames(caller, fieldname):
            return 
        if fieldname == "name":
            self.key = value
        else:
            caller.chardata[fieldname] = value
        caller.update_charsheet()
        caller.msg("%s was set to %s." % (fieldname, value))


class CmdGMsheet(MuxCommand):
    """
    GM-modification of char sheets

    Usage:
      @gmsheet character [= fieldname value]

    Switches:
      lock - lock the character sheet so the account
             can no longer edit it (GM's still can)
      unlock - unlock character sheet for Account 
             editing.

    Examples:
      @gmsheet Tom
      @gmsheet Anna = str 12 
      @gmsheet/lock Tom

    """
    key = "gmsheet"
    locks = "cmd: perm(Admins)"
    help_category = "RP"

    def func(self):
        caller = self.caller
        if not self.args:
            caller.msg("Usage: @gmsheet character [= fieldname value]")
             
        if self.rhs:
            # rhs (right-hand-side) is set only if a '=' 
            # was given.
            if len(self.rhs) < 2:
                caller.msg("You must specify both a fieldname and value.")
                return  
            fieldname, value = self.rhs.split(None, 1)
            fieldname = fieldname.lower()
            if not _validate_fieldname(caller, fieldname):
                return           
            charname = self.lhs
        else:
            # no '=', so we must be aiming to look at a charsheet
            fieldname, value = None, None
            charname = self.args.strip()
        
        character = caller.search(charname, global_search=True)
        if not character:
            return
        
        if "lock" in self.switches:
            if character.db.sheet_locked:
                caller.msg("The character sheet is already locked.")
            else:
                character.db.sheet_locked = True
                caller.msg("%s can no longer edit their character sheet." % character.key)
        elif "unlock" in self.switches:
            if not character.db.sheet_locked:
                caller.msg("The character sheet is already unlocked.")
            else:
                character.db.sheet_locked = False 
                caller.msg("%s can now edit their character sheet." % character.key)

        if fieldname:
            if fieldname == "name":
                character.key = value
            else:
                character.db.chardata[fieldname] = value
            character.update_charsheet()
            caller.msg("You set %s's %s to %s." % (character.key, fieldname, value)
        else:
            # just display
            caller.msg(unicode(character.db.charsheet))
