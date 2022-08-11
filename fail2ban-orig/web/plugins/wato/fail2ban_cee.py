#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

try:
    from cmk.gui.i18n import _
    from cmk.gui.plugins.wato import (
        HostRulespec,
        rulespec_registry,
    )
    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import RulespecGroupMonitoringAgentsAgentPlugins
    from cmk.gui.valuespec import (
        Age,
        Alternative,
        Dictionary,
        FixedValue,
    )
    def _valuespec_agent_config_fail2ban():
        return Alternative(
            title = _("Fail2Ban"),
            help = _("This will deploy the agent plugin <tt>fail2ban</tt> "
                     "for checking failed login attempts."),
            style = "dropdown",
            elements = [
                Dictionary(
                    title = _("Deploy the fail2ban plugin"),
                    elements = [
                        ( "interval", Age(title = _("Run asynchronously"), label = _("Interval for collecting data"), default_value = 300 )),
                    ],
                ),
                FixedValue(None, title = _("Do not deploy the fail2ban plugin"), totext = _("(disabled)") ),
            ]
        )
    rulespec_registry.register(
         HostRulespec(
             group=RulespecGroupMonitoringAgentsAgentPlugins,
             name="agent_config:fail2ban",
             valuespec=_valuespec_agent_config_fail2ban,
         ))

except ModuleNotFoundError:
    # RAW edition
    pass