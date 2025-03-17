from skills import SKILLS

class SkillOrchestrator:
    def execute_skill(self, skill_name):
        if skill_name not in SKILLS:
            return "Skill not found", {}

        result, metrics = SKILLS[skill_name]()
        return result, metrics

    def execute_meta_skill(self, skill_sequence):
        results = []
        for skill in skill_sequence:
            result, _ = self.execute_skill(skill)
            results.append(result)
        return results
