#ifndef SAGE_ENTITY_HPP
#define SAGE_ENTITY_HPP

#include "sage/dtype/dtype.hpp"
#include "sage/graph/item.hpp"
#include "sage_pch.hpp"

namespace sage {
class Entity {
 private:
  item::Scope m_Scope;
  item::Type m_Type;
  item::Prop m_Prop;

 public:
};
}  // namespace sage
#endif  // !SAGE_ENTITY_HPP