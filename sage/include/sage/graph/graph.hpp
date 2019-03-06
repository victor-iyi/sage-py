#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace graph {

    class SAGE_API Edge {
     public:
      Edge(std::string leftEntityId, std::string rightEntityId,
           std::string relationId, std::string qualifierRelationId,
           std::string qualifierEntityId)
          : _m_LeftEntityId(leftEntityId),
            _m_RightEntityId(rightEntityId),
            _m_RelationId(relationId),
            _m_QualifierRelationId(qualifierRelationId),
            _m_QualifierEntityId(qualifierEntityId) {
              if (_m_RelationId != "iclass") {
                // assert len({self.leftEntityId, self.rightEntityId,
                // self.qualifierEntityId}) == 3
              }
            }

      const char* type() const;
      void invert();
      std::tuple<std::string> nodes();

     private:
      size_t _m_edgeId = 0;
      std::string _m_LeftEntityId, _m_RightEntityId, _m_RelationId,
          _m_QualifierRelationId, _m_QualifierEntityId;
    };

    class SAGE_API EdgeList {
     public:
      EdgeList() {}
      size_t size() const;

     private:
      std::vector<Edge> _m_List;
    };

    class SAGE_API SemanticGraph {
     public:
      SemanticGraph() {}

     private:
    };

  }  // namespace graph
}  // namespace sage

#endif  // !SAGE_GRAPH_HPP